import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def find_inverse(l):
    result = []
    for i in l:
        result.append(1/i)
    return result

def find_mul(l, m):
    result = []
    for i, j in zip(l, m):
        result.append(i*j)
    return result

def find_exp(l):
    result = []
    for i in l:
        result.append(math.exp(i))
    return result

def find_sum(l):
    result = 0
    for i in l:
        result += i
    return result

def regression(n, x, y):
    x_inverse = find_inverse(find_mul(x,x))
    y_inverse = find_inverse(y)
    x_squared = find_mul(x_inverse,x_inverse)
    xy = find_mul(x_inverse, y_inverse)

    xy_sum = find_sum(xy)
    x_squared_sum = find_sum(x_squared)
    x_sum = find_sum(x_inverse)
    y_sum = find_sum(y_inverse)

    b = (y_sum*x_squared_sum-xy_sum*x_sum)/(n*x_squared_sum-x_sum**2)
    a = (y_sum-n*b)/x_sum
    result = []
    result.append(a/b)
    result.append(1/b)

    def function(xx):
        return (1/b)*(xx**2)/((a/b)+xx**2)
    plot(x, y, function)

    return result

def plot(xList,yList,func,sharpness=1000,marginPercentage=2):
    plt.scatter(xList,yList,color="red",marker=1)
    range=max(xList)-min(xList)
    xListNew=list(np.linspace(min(xList)-range*marginPercentage/100,max(xList)+range*marginPercentage/100,sharpness))
    yListNew=[func(x) for x in xListNew]


    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    plt.plot(xListNew, yListNew)
    plt.show()

f = open("data.txt", "r")
x = []
y = []
z = []
for i in f:
    z.append(i)

for j in z:
    c = j.split()
    x.append(float(c[0]))
    y.append(float(c[1]))

n = len(x)
arr = regression(n, x, y)

for i in arr:
    print(i)
