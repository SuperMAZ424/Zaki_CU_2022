import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

S= np.linspace(0,1600,50)
func_S = []
for n in S:
    alpha = 2.46 #S^-1
    beta = 83.05 #nM
    func_e_S = (alpha*n)/(beta+n)
    func_S.append(func_e_S)
plt.plot(S,func_S)
plt.show()


'''
def odes_2(on, t):

    alpha = -2.46  # S^-1
    beta = 83.05  # nM
    S = on[0]
    if S > (100.0*beta):
        dSdt = alpha
    elif S < (100.0*beta):
        dSdt = alpha*S/beta

    return [dSdt]

on = [x0[5]]
S = on[:,0]
print(float(on[0]))
print(odes_2(on=float(on[0]), t=0))
'''
