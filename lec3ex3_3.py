import numpy as np
import matplotlib.pyplot as plt

def absolute(val):
    if val >=0:
        return val
    elif val < 0:
        return -1 * val
    
T = 200
alpha = 0.9 


x = np.empty(T+1)

x[0] = 0

for t in range(T):
    x[t+1] = alpha*np.absolute(x[t]) + np.random.randn()

plt.plot(x)
plt.show()