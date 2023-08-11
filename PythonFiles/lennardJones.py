import numpy as np
import matplotlib.pyplot as plt

# The Lennard-Jones parameters:
A = 1.024e-23   # J.nm^6
B = 1.582e-26   # J.nm^12

# Adjust the units of A and B - they have more manageable values
# in K.nm^6 and K.nm^12
kB = 1.381e-23  # Boltzmann's constant, J/K
A, B = A / kB, B / kB

# Interatomic distance, in nm
r = np.linspace(0.3, 1., 1000)
# Interatomic potential
U = B/r**12 - A/r**6

plt.plot(r, U, 'k', lw=2., label='Lennard-Jones')

plt.xlim(0.3, 0.6)
plt.ylim(-120, 0)
plt.xlabel('r / nm')
plt.ylabel('Potential energy / K')

plt.legend(loc=4)

plt.show()