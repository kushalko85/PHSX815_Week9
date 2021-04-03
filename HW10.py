import numpy as np
from scipy import optimize


#define function

def f(x):

    return (x[0]**2+ 2*x[1]**2 +5)


#Brent's Minimization method

BM = optimize.fmin(f,[0,1])
Fmin = BM[0]**2 + 2*BM[1]**2 + 5
#print(BM)
#minima = BM.x
print("The minimum of the function (x[0]**2+ 2*x[1]**2 +5) is at (%.3f, %.3f,%.2f)" %(BM[0],BM[1],Fmin))
