'''Given an array of integers, calculate the fractions of its elements that are positive, negative, 
and are zeros. Print the decimal value of each fraction on a new line.'''

#!/bin/python

import sys
from decimal import *

n = int(input().strip())
arr = map(int,input().strip().split(' '))

a = len(arr)
zero = 0
pos = 0
neg = 0

for i in arr:
    if i == 0:
        zero += 1
    elif i < 0:
        neg += 1
    else:
        pos += 1

p = Decimal(pos) / Decimal(a)
s = Decimal(neg) / Decimal(a)
z = Decimal(zero) / Decimal(a)

print p
print s
print z

