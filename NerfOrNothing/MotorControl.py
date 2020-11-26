import RPi.GPIO as GPIO
import math
import time
from ProjectileMotion import ArcCalc

Earth = ArcCalc(9.8)

motorPins = (12, 16, 18, 22)    # define pins connected to four phase ABCD of stepper motor
CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  # define power supply order for rotating clockwise

def setup():    
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT)
        
# as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):      # cycle for power supply order
        for i in range(0,4,1):  # assign to each pin
            if (direction == 1):# power supply order clockwise
                GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              # power supply order anticlockwise
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)    
        

def moveSteps(direction, ms, angle):
    steps = int((512 /(math.tau))*(angle))
   
    oppositeDir = (direction + 1) % 2
    for i in range(steps):
        moveOnePeriod(direction, ms)
    time.sleep(1)
    for i in range(steps):
        moveOnePeriod(oppositeDir, ms)
        

def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],GPIO.LOW)
            


def destroy():
    GPIO.cleanup()   

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        #xDis = input("Input horizontal distance ")
        #yDis = input("Input vertical distance ")
        #optAngle = Earth.plotArc(10, xDis, yDis)
        moveSteps(0, 3, 1)
        destroy()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
