import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


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
    x_squared = find_mul(x, x)
    exp_x = find_exp(x)
    exp_squared = find_mul(exp_x, exp_x)
    xy = find_mul(x, y)
    expy = find_mul(exp_x, y)
    expx_mul = find_mul(exp_x, x)
    expx_squared = find_mul(expx_mul, expx_mul)

    xy_sum = find_sum(xy)
    exp_x_sum = find_sum(exp_x)
    x_squared_sum = find_sum(x_squared)
    exp_squared_sum = find_sum(exp_squared)
    expy_sum = find_sum(expy)
    expx_sum = find_sum(expx_mul)
    # expx_squared_sum = find_sum(expx_squared)

    b = (xy_sum*expx_sum-expy_sum*x_squared_sum)/(expx_sum**2-exp_squared_sum*x_squared_sum)
    a = (xy_sum-b*expx_sum)/x_squared_sum
    result = []
    result.append(1/a)
    result.append(1/b)

    def function(xx):
        return (1/a)*xx+(1/b)*math.exp(xx)
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
