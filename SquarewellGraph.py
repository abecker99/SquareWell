import matplotlib.pyplot as plt
import numpy as np

z_o = ((1*10**-10)/(1.0546*10**-34))*np.sqrt(2*(9.109*10**-31)*(4.0*10**-17))

x = np.linspace(0,10,1000)
#funct vvv
y_1 = np.sqrt((z_o/x)**2-1) - np.tan(x)
y_2 =  np.sqrt((z_o/x)**2-1) + (1/np.tan(x))

plt.plot(x, y_1)
plt.plot(x, y_2)

plt.ylim([-8, 8])
plt.show()
# plt.savefig("tan.pdf")