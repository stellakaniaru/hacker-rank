'''Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
 Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.'''

#!/bin/python3

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time1 = datetime.strptime(s, "%I:%M:%S%p")
    time2 = datetime.strftime(time1, "%H:%M:%S")
    return time2

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
