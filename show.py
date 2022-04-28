import numpy as np
import matplotlib.pyplot as plt




x = range(0,10)
y =[ 1.8*f + 32*25 for f in x]


print(f'X: {x}')
print(f'Y: {y}')
plt.plot(x,y,'-*r')
plt.show()

