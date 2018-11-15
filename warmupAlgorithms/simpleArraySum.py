#!/bin/python

import sys

#get the input
n = int(input().strip())

#split items in the input ans store in an array
arr = map(int,input().strip().split(' '))

#find the sum of the items in the array
total = 0
for i in arr:
    total += i
print (total)
    
