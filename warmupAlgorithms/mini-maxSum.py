'''Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers. Then print the respective minimum 
and maximum values as a single line of two space-separated long integers.'''

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
from itertools import combinations

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    list_sum = []
    combine_list = combinations(arr, 4)
    for i in combine_list:
        list_sum.append(sum(i))
    print("{} {}".format(min(list_sum), max(list_sum)))
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
