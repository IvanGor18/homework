import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

divid = 0

a,b = 1,1 
# a,b = 2,1
# a,b = 1,2

x1 = np.linspace(-200, divid-0.001, 10000)
x2 = np.linspace(divid+0.001, 200, 10000)

def f(x):
    return 1+(a/x)**b


fig, ax = plt.subplots(figsize=(16, 10))
ax.plot(x1, f(x1), linewidth=2)
ax.plot(x2, f(x2), linewidth=2)
ax.set_xlim(-2,2)
ax.set_ylim(-10,10)

axins1 = inset_axes(ax, width="40%", height="40%", loc='lower right')
axins1.plot(x1, f(x1), label='Для Малых x', linewidth=2)
axins1.plot(x2, f(x2), linewidth=2)
axins1.set_xlim(-2, 2)
axins1.set_ylim(-20, 20)
axins1.set_title('Для малых x')
   
axins2 = inset_axes(ax, width="40%", height="40%", loc='upper right')
axins2.plot(x1, f(x1), label='', linewidth=2)
axins2.plot(x2, f(x2), label='', linewidth=2)
axins2.set_xlim(-10, 10)
axins2.set_ylim(-100, 100)
axins2.set_title('Для больших x')

ax.axvline(divid, color='red', linestyle='--', label='Точка разрыва')
axins1.axvline(divid, color='red', linestyle='--', label='Точка разрыва')
axins2.axvline(divid, color='red', linestyle='--', label='Точка разрыва')

ax.set_title(r'$f(x)=\frac{x^{\beta}+\alpha^{\beta}}{x^{\beta}}$')


ax.grid(True)
axins1.grid(True)
axins2.grid(True)
#plt.savefig(dir + '/my_first_dependence.png', dpi=600)
plt.show()
