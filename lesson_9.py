import matplotlib.pyplot as plt
import numpy as np
import os 

dir = os.getcwd()

a,b = 1,1 

x1 = np.linspace(-2, 0, 100)
x2 = np.linspace(0, 2, 100)

def f(x):
    return (x**b + a**b)/x**b

line1 = plt.plot(x1, f(x1))
line2 = plt.plot(x2, f(x2))

plt.plot(x1, f(x1), color = 'b')
plt.plot(x2, f(x2), color = 'b')

plt.xlabel('X')
plt.ylabel('Y')

plt.savefig(dir + '/my_first_dependence.png', dpi=600)

plt.grid(True)
plt.show()
