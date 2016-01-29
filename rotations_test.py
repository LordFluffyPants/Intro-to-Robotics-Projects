import numpy as np

from rotations import *

#Question 4
matrix = np.array([ [ 0.7474 ,    0.5430,    0.3826  ],
                    [ -0.2936,    0.7867,    -0.5430 ],
                    [ -0.5960,    0.2936,    0.7474  ]])
print "matrix=",matrix
qv = M2Q(matrix)
print "qv=",qv


#Question 5
qv = np.array([0.74846,0.13062,0.50764,0.40626])
print "qv=",qv
matrix = Q2M(qv)
print "matrix=",matrix
