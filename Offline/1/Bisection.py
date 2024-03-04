import math
from typing import List, Any, Union

import matplotlib.axes as ax
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# def f(y):
# return ((y / (1 - y)) * (6.0 / (2 + y))**0.5) - 0.05

def f(y):
    return 3.1416*y*y*y-3*3.1416*3*y*y+12

def bisection(lower_bound, upper_bound, max_error, max_iter):
    i = 1
    temp = None
    while i != max_iter:
        mid_value = (lower_bound + upper_bound) / 2
        if temp is not None:
            error = (abs(temp - mid_value) / mid_value) * 100
            if error <= max_error:
                return mid_value
        temp = mid_value
        if f(lower_bound) * f(mid_value) == 0:
            return mid_value
        elif f(lower_bound) * f(mid_value) < 0:
            upper_bound = mid_value
            i = i + 1
        elif f(upper_bound) * f(mid_value) < 0:
            lower_bound = mid_value
            i = i + 1

    if i == max_iter:
        print("root not found")


def tabulation(lower_bound, upper_bound, max_error, max_iter):
    i = 1
    temp = None
    p, q, r = [], [], []
    r.append(None)
    while i != max_iter:
        p.append(i)
        mid_value = (lower_bound + upper_bound) / 2
        q.append(mid_value)
        if temp is not None:
            error = (abs((temp - mid_value) / mid_value)) * 100
            r.append(error)
            if error <= max_error:
                break
        temp = mid_value
        if f(lower_bound) * f(mid_value) == 0:
            break
        elif f(lower_bound) * f(mid_value) < 0:
            upper_bound = mid_value
            i = i + 1
        elif f(upper_bound) * f(mid_value) < 0:
            lower_bound = mid_value
            i = i + 1
    data = {'Iteration': p, 'Estimated Value': q, 'Error%': r}
    table = pd.DataFrame(data)
    print(table)

def plot ():
    val = np.linspace(-10, 5, 4000)
    funval = f(val)
    val = list(val)
    funval = list(funval)
    for index in range(len(funval)-1):
        if abs(funval[index] - funval[index+1]) > 10:
            val[index] = np.nan
            funval[index] = np.nan

    plt.plot(val, funval)
    plt.grid(True, which='both')
    plt.ylim(-10, 10)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


a = 0
b = 1
x = bisection(a, b, 0.5, 100)
tabulation(a, b, 0.5, 100)
plot()
print('The Estimated Root is: ', x)
