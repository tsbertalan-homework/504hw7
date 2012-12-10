
# code online at https://github.com/tsbertalan-homework/504hw7

import numpy as np
sqrt = np.sqrt
import matplotlib.pyplot as plt
fig = plt.figure(1, figsize=(11.5, 8))
ax = fig.add_subplot(1, 1, 1)

b = 0.1

zmin = .0001
zmax = 1
resolution = 10000
dz = (zmax - zmin) / resolution
ul = [1]
ml = [-sqrt(2 - 2 * b * np.log((b + 1) / b))]
zl = [0]
for i in range(resolution):
    z = zl[i]
    u = ul[i]
    m = ml[i]
    zl.append(z + dz)
    ul.append(u + m * dz)
    ml.append(m + u ** 2 / (b + u) * dz)

z_true = list(np.arange(zmin, zmax, dz))
uf = lambda u: 1 - z * sqrt(2) + z ** 2 / 2
u_true = [uf(z) for z in z_true]
 
ax.plot(zl, ul, 'k-', label='Euler-integrated')
ax.plot(z_true, u_true, 'k--', label=r'$F_o(u)$ approximation')

ax.set_xlabel(r'$z = x / \sqrt{C_0\mathcal{D}/V}$, dimensionless position')
ax.set_ylabel(r'$u = C/C_0$, dimensionless concentration')
ax.set_title('HW 7, No. 1, part i')
ax.legend()

fig.savefig('hw7-1i.pdf')

plt.show()