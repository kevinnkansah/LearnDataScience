import numpy as np
import matplotlib.pyplot as plt


axes = plt.axes(projection='3d')

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

axes.plot(x, y, z)
axes.set_title('DAAAAMNN SHORTY')
plt.show()
