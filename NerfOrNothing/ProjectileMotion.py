import math
import numpy as nu
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

class ArcCalc():
    gravity = 0
    angle = 0

    def __init__(self, gravity):
        self.gravity = gravity

    def optAngle(self, startVelocity, startHeight):
        optimalAngle = math.asin((2*(((startHeight * self.gravity)/startVelocity**2) + 1))**(-0.5))
        self.angle = optimalAngle
        return optimalAngle
    
    def maxDistance(self, startVelocity, startHeight):

        self.optAngle(startVelocity, startHeight)
        print(math.degrees(self.angle))

        a = -0.5 * self.gravity
        b = startVelocity * math.sin(self.angle)
        c = startHeight

        timeInAir = max(((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)), ((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)))

        distance = startVelocity * math.cos(self.angle) * timeInAir

        print(distance)

        return distance

    def angleForXY(self, startVelocity, xPos, yPos):

        point = (startVelocity**2 - math.sqrt(startVelocity**4 - self.gravity*(self.gravity*xPos**2 + 2*yPos*startVelocity**2)))/(self.gravity*xPos)

        self.angle = math.atan(point)

        print(math.degrees(self.angle))

        return point

    def plotArc(self, *args):
        t = nu.linspace(0, 10, 1000)
        fig = plt.figure()
        ax = fig.gca(projection="3d")


        if len(args) == 2:
            self.maxDistance(args[0], args[1])
            plotY = args[0] * math.sin(self.angle) * t - 1/2 * self.gravity * t**2 + args[1]
        
        elif len(args) == 3:
            self.angleForXY(args[0], args[1], args[2])
            #ax.plot(args[1], 0, args[2], "rx")
            plotY = args[0] * math.sin(self.angle) * t - 1/2 * self.gravity * t**2

        else:
            return(print("Wrong number of args"))
            
        plotX = args[0] * math.cos(self.angle) * t
        
        plotY = plotY[plotY > 0]
        plotX = plotX[0: len(plotY)]
        t = t[0: len(plotY)]

        #ax.plot(plotX,t*0, plotY, "b--")
        #ax.set_xlim3d(0, max(plotX)+3)
        #ax.set_ylim3d(-(max(plotX)/2), max(plotX)/2)
        #ax.set_zlim3d(-1, max(plotX)+3)
        #ax.plot(plotX[len(plotY)-1], plotY[len(plotY)-1], "gx")
        #plt.show()

        return(self.angle)
        



#Earth = ArcCalc(9.8)
#Earth.plotArc(10, 4, 3)
    