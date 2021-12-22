'''Program to find L and U matrix using LU decomposition.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
# To print L and U matrix
import numpy as np
from scipy.linalg import lu
A=np.array(eval(input()))
P,L,U=lu(A)
print(L)
print(U)