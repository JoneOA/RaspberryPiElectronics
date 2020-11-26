import matplotlib.pyplot as plt
import numpy as nu
import math

a = 0
b = 0
c = 0

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 *a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 *a)

    return(max(x1, x2))

def timeInAir(h, v1, g):
    x = nu.linspace(-0, 100, 1000)
    p = nu.arange(0., 5., 0.2)

    ang = math.asin((2*(((h * g)/v1**2) + 1))**(-0.5))
    #print(ang)
    a = -0.5 * g
    b = v1 * math.sin(ang)
    c = h

    l = v1*math.cos(ang) * x
    k = a*x**2 + b*x + c

    timeUp = quadratic(a, b, c)

    print(timeUp)

    dis = v1 * math.cos(ang) * timeUp

    timeMaxHeight = (v1 * math.sin(ang))/g
    maxHeight = (v1**2 * (math.sin(ang))**2)/(2 * g) + h
    disMaxHeight = v1 * math.cos(ang) * timeMaxHeight
    #print(timeMaxHeight)
    #print(maxHeight)
    #print(dis)
    q = 3
    y = 20

    point = (v1**2 + math.sqrt(v1**4 - g*(g*q**2 + 2*y*v1**2)))/(g*q)

    angle = math.atan(point)

    j = v1*math.cos(angle)*x
    m = a*x**2 + (v1*math.sin(angle)*x) + c



    plt.xlim(-1, dis + 5)
    plt.ylim(-1, dis + 5)
    plt.xlabel('Distance'); plt.ylabel('Height')
    plt.plot(x, x*0, 'green')
    plt.plot(j, m, 'b--')
    plt.plot(dis, 0, "rx")
    plt.plot(q, h+y, "rx")
    plt.show()

    return dis

def distance(v1, angle, t):
    return(v1*math.cos(angle)*t)

timeInAir(2, 20, 9.8)