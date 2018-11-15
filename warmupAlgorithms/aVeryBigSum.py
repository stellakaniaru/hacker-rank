#!/bin/python

import sys

#get the input
n = int(input().strip())

#split the elements in the input into the array
arr = map(int,input().strip().split(' '))

#get the total of the items and display it to the console
total = 0
for i in arr:
    total += i
print (total)
