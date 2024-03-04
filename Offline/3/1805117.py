import math
import pandas

def f(time):
    return (2000*math.log(140000/(140000-2100*time)))-9.8*time

def trapezoidal(a, b, n):
    points = []
    values = []

    interval = (b-a)/n
    for i in range(n+1):
        points.append(a+i*interval)
        values.append(f(points[i]))

    sum = 0
    for j in range(n):
        temp = interval/2
        temp = temp*(values[j]+values[j+1])
        sum = sum + temp
    return sum


def simpson1_3(a, b, n):
    points = []
    values = []

    interval = (b-a)/n
    for i in range(n+1):
        points.append(a+i*interval)
        values.append(f(points[i]))
       
    sum = 0
    for j in range(0, n-1, 2):
        temp = interval/3
        temp = temp*(values[j]+4*values[j+1]+values[j+2])
        sum = sum + temp

    return sum


def printError(method, a, b):
    relativeError = []
    relativeError.append(None)
    values = []
    n = []
    
    if method == 1:
        for i in range(5):
            n.append(i+1)
            values.append(trapezoidal(a, b, i+1))
    elif method == 2:
        for i in range(5):
            n.append(2*(i+1))
            values.append(simpson1_3(a, b, 2*i+2))
            
    for j in range(4):
        difference = abs(values[j+1] - values[j])
        relativeError.append((difference/values[j+1])*100)

    print('Absolute approximate relative erros for n=1 to n=5:')
    data = {'Value of n': n, 'Estimated Value':values, 'Error%':relativeError}
    df = pandas.DataFrame(data)
    print(df)

num_Interval = input()
print('In trapezoidal rule of numerical integration:')
distance_trap = trapezoidal(8, 30, int(num_Interval))
print('Estimated distance when n = ', num_Interval, ': ', distance_trap)
print()
printError(1, 8, 30)
print()
print('In Simpson\'s 1/3rd rule of numerical integration:')
distance_simpson = simpson1_3(8, 30, int(num_Interval)*2)
print('Estimated distance when n = ', num_Interval, ': ', distance_simpson)
print()
printError(2, 8, 30)
