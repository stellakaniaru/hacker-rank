'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.'''

#!/bin/python

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_temp = map(int,input().strip().split(' '))
    a.append(a_temp)
    
d1 = sum([a[i][i] for i in range(len(a))])
d2 = sum([a[(len(a) - 1 - i)][i] for i in range(len(a) - 1, -1, -1)])

diff = d1 - d2

print abs(diff)
