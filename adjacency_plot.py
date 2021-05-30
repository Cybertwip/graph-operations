import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


input_values = np.random.rand(2)  # 2 different values
m = np.random.choice(input_values, (2, 2))  # 100 cells, each with one o the 8 values

# Matrix is:
'''
010011
101010
010100
001010
110101
100010

'''
m = []
m.append([0, 1, 0, 0, 1, 1])
m.append([1, 0, 1, 0, 1, 0])
m.append([0, 1, 0, 1, 0, 0])
m.append([0, 0, 1, 0, 1, 0])
m.append([1, 1, 0, 1, 0, 1])
m.append([1, 0, 0, 0, 1, 0])

data = m

# create discrete colormap
cmap = colors.ListedColormap(['blue', 'gray'])
bounds = [0,1]

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap)

# draw gridlines
ax.grid(which='minor', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(0, 6, 1));
ax.set_yticks(np.arange(0, 6, 1));

plt.gca().invert_yaxis()

plt.show()