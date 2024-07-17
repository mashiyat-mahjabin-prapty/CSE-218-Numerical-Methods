import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def lagrangian_interpolate(x, f, new_X, n):
  
    result = 0.0
    for i in range(n):
  
        term = f[i]
        for j in range(n):
            if j != i:
                term = term * (new_X - x[j]) / (x[i] - x[j])
  
        result += term

    return result

def error_calculation(value1, value2):
    vol1 = [25, 27, 30]
    vol2 = [30, 31, 35]
    pres1 = [43, 42, 40]
    pres2 = [40, 35, 30]

    val28 = lagrangian_interpolate(vol1, pres1, 28, 3)
    val32 = lagrangian_interpolate(vol2, pres2, 32, 3)

    error28 = ((value1-val28)/value1)*100
    error32 = ((value1-val32)/value2)*100
    print('Error for 28 sec is: ', error28)
    print('Error for 32 sec is: ', error32)


volume1 = [22, 25, 27, 30]
pressure1 = [44, 43, 42, 40]
pressure2 = [40, 35, 30, 25]
volume2 = [30, 31, 35, 37]

f28 = lagrangian_interpolate(volume1, pressure1, 28, 4)
f32 = lagrangian_interpolate(volume2, pressure2, 32, 4)

print(f28)
print(f32)

error_calculation(f28, f32)

integrate_values_pressure1 = [43, 42, 40]
integrate_values_pressure2 = [40, 35, 30]
integrate_values_volume1 = [25, 27, 30]
integrate_values_volume2 = [30, 31, 35]
x = Symbol('x')
f1 = lagrangian_interpolate(integrate_values_volume1, integrate_values_pressure1, x, 3)
f2 = lagrangian_interpolate(integrate_values_volume2, integrate_values_pressure2, x, 3)
f1_prime = integrate(f1, (x, 25, 30))
f2_prime = integrate(f2, (x, 30, 35))
print(f1)
print(f2)
print(f1_prime+f2_prime)



plt.plot(volume1, pressure1, 'b', label = 'P1')
plt.plot(volume2, pressure2, 'r', label = 'P2')
plt.plot(28, f28)
plt.plot(32, f32)

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

