import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', linestyle='--', color='blue')
plt.plot(x, y2, label='cos(x)', linestyle='-.', color='red')

plt.fill_between(x, y1, y2, where=(y1 > y2), color='gray', alpha=0.5)

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin(x) and Cos(x) between 0 and 2pi with hatched pattern')
plt.grid(True)

plt.show()
