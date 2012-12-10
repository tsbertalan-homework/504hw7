import numpy as np
sqrt = np.sqrt
ln = np.log
import matplotlib.pyplot as plt

fig = plt.figure(1, figsize=(16, 8))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

bl = list(np.arange(0.001, 10, .001))

# true solution
z0f = lambda b: -sqrt(2 - 2 * b * ln( (b + 1) / b))
z0l = [z0f(b) for b in bl]
ax1.plot(bl, z0l, 'k-', label='part c')

# F_0(u) approximation
ax1.scatter([0], [-sqrt(2)], color='k', label=r'part d: $u/(b+u) = F_0(u) \approx 1$' +
                '\n' + r'(only valid around $b=0$)')


z0f0 = lambda b: -1 / sqrt(b)
z0l0 = [z0f0(b) for b in bl]
ax1.plot(bl, z0l0, 'k--', label=r'part f: $u/(b+u) = F_1(u) \approx u / b$')

ax1.set_xlabel(r'parameter $b$', fontsize=14)
ax1.set_ylabel(r'initial gradient, $\frac{\partial u}{\partial z} | _{z=0}$', fontsize=14)
ax1.legend(loc='best')
ax1.set_xlim((-.1, 12))
ax1.set_ylim((-1.6, 0))

# examine true solution at low b
ax2.set_xlabel(r'parameter $b$')
ax2.plot(bl, z0l, 'k-', label='part c')
ax2.set_xlim((0.001, .02))
ax2.set_ylim((-1.5, -1.3))
ax2.legend(loc='best')

fig.suptitle('HW 7, No. 1, part c/d/f', fontsize=16)
fig.savefig('hw7-1c.pdf')

#plt.show()