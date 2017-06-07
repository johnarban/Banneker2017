"""
Demonstrates a few common tricks with shaded plots.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, Normalize

"""Display a correct numeric colorbar for a shaded plot."""
y, x = np.mgrid[-4:2:200j, -4:2:200j]
z = 10 * np.cos(x**2 + y**2)

cmap = plt.cm.copper
ls = LightSource(315, 45)
rgb = ls.shade(z, cmap)

fig, ax = plt.subplots()
ax.imshow(rgb)

# Use a proxy artist for the colorbar...
im = ax.imshow(z, cmap=cmap)
im.remove()
fig.colorbar(im)

ax.set_title('Using a colorbar with a shaded plot', size='x-large')

plt.show()