#!/bin/python

import sys

#get the input
a0,a1,a2 = input().strip().split(' ')
tripa = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
tripb = [int(b0),int(b1),int(b2)]

#function to compare the items in both arrays
def triplets(a, b):
    totA = 0
    totB = 0
    for i in range(len(a)):    
        if a[i] > b[i]:
            totA += 1
        elif b[i] > a[i]:
            totB += 1
    return totA, totB

print ("%d %d"%(triplets(tripa,tripb)))

