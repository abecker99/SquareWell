import numpy as np
import matplotlib.pyplot as plt

def find_sign_change(f, step, a, b):
    x = a
    pairs = []
    while (x + step < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x, x+step])
        x += step
    return pairs

zeros = []
def bisect(f, pairs, tolerance):
    
    for pair in pairs:
        midpoint = (pair[1] - pair[0])/2 + pair[0]
        iter = 1
        max_iter = 1000
        while (abs(f(midpoint)) > tolerance and iter < max_iter):
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint
            midpoint = (pair[1] - pair[0])/2 + pair[0]
            iter +=1
        if (iter < max_iter):
            zeros.append(midpoint)
    return zeros
#zeros are z, need to compute energy with it    

# def sinc(x):
#     if (x == 0):
#         return 1
#     else:
#         return np.sin(x)/x

def eq8_13(x):
    z_o = ((1*10**-10)/(1.0546*10**-34))*np.sqrt(2*(9.109*10**-31)*(8.0*10**-17))
    return np.sqrt((z_o/x)**2-1) - np.tan(x)

def eq8_14(x):
    z_o = ((1*10**-10)/(1.0546*10**-34))*np.sqrt(2*(9.109*10**-31)*(8.0*10**-15))
    return np.sqrt((z_o/x)**2-1) + (1/(np.tan(x)))

pairs = find_sign_change(eq8_13, 0.1, 0, 10)
print("symmetric: ", pairs)
zeros = bisect(eq8_13, pairs, 1E-10)

pairs = find_sign_change(eq8_14, 0.1, 0, 10)
print("asymmetric: ", pairs)
zeros = bisect(eq8_14, pairs, 1E-10)
print("zeros: ", zeros)

def E(zeros):
    E_n = []
    for zero in zeros:
        z = zero
        E = (((1.0546*10**-34)**2)*(z**2))/(2*(9.109*10**-31)*((1*10**-10)**2)) - (8.0*10**-15)
        E_n.append(E)
    return E_n

def E_infinite(N):
    E_in = []
    for N in range(0,N):
        E_i = ((N**2)*(np.pi**2)*(1.0546*10**-34)**2)/(8*(9.109*10**-31)*((1*10**-10)**2)) - (8.0*10**-15)
        E_in.append(E_i)
    return E_in

Infinite = E_infinite(5) #5 for normal
finite = E(zeros)

x_ = np.linspace(-8*10**-15,-7.98*10**-15,1000)
y = x_*1
print(finite)
print(Infinite)

plt.plot(finite, Infinite)
plt.plot(x_, y)
plt.axis('square')
plt.show()

#changing vo, shift range to 0 - zo
#energies close but not quite > deeper well better but not exactly
#slope of 1 = same energies plotted against themselves