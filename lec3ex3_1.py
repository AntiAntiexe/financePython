import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha = [0, 0.8, 0.98]


x = np.empty(T+1)



for alp in alpha:
    x[0] = 0
    for t in range(T):
        x[t+1] = alp*x[t] + np.random.randn()
    plt.plot(x)

#plt.plot(x)
plt.legend(alpha)
plt.title('How elipson shocks of (E) affect a normal PDF')
plt.ylabel('x value')
plt.xlabel('value of T')
plt.show()



