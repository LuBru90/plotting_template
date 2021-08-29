# %% Imports:
import matplotlib.pyplot as plt
import numpy as np

# Data:
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x - np.pi/8)

# %% Plotting:
fsize = 11
plt.close('all')

fig, ax = plt.subplots()

ax.plot(x, y, color='royalblue', label='sin', zorder = 2)
ax.plot(x, y2, color='goldenrod', label='cos', zorder = 3)
ax.plot(x, y3, color='sienna', label='sin2', zorder = 4)
ax.plot(x, y3/2, marker='x', linewidth=0, color='sienna', label='sin2', zorder = 4)
ax.set_xlabel('x Label', fontsize=fsize)
ax.set_ylabel('y Label', fontsize=fsize)

plt.xticks(fontsize=fsize);
plt.yticks(fontsize=fsize);
plt.grid(zorder = 1, alpha = 0.5)
plt.legend(framealpha = 1, fontsize = fsize, loc = 'upper right')

fig.show()
plt.savefig('out.jpg', dpi=200)
input()
