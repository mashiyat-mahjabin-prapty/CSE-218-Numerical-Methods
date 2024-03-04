import math
import pandas as pd

def f(y):
    temperature = 19+273.15
    a0 = temperature*1.129241*(10**(-3))
    a1 = temperature*2.341077*(10**(-4))
    a3 = temperature*8.775468*(10**(-8))
    NaN = float('NaN')
    if y == 0 or y == 1:
        b = NaN
    else:
        b = math.log(y)

    return a0+a1*b+a3*(b**3)-1

def bisection(lower, upper):
    i = 1
    temp = None
    p, q, r = [], [], []
    r.append(None)
    result = None
    while i != 100:
        mid = (lower+upper)/2
        p.append(i)
        q.append(mid)
        if temp is not None:
            error = (abs((mid-temp)/mid))*100
            r.append(error)
            if error <= 0.5:
                result = mid
                break
        temp = mid

        midfun = f(mid)
        lofun = f(lower)

        if midfun*lofun == 0:
            result = mid
            break
        elif midfun*lofun < 0:
            upper = mid
            i = i+1
        else:
            lower = mid
            i = i+1
    if i == 100:
        print('Root not found in 100 iterations')
    data = {'Iteration': p, 'Estimated Value': q, 'Error%': r}
    table = pd.DataFrame(data)
    print(table)
    return result



lower_bound = 14000
upper_bound = 16000

x = bisection(lower_bound, upper_bound)
print('The root is ', x)
