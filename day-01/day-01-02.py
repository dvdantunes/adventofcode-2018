#!/usr/bin/python

''' Advent of code - Day 1: Chronal Calibration - Problem 1.2

https://adventofcode.com/2018/day/1#part2
'''

import os, sys



# Reading file
filename = 'input1.txt'
lines = []
input_file_path = "%s/%s" % (os.path.abspath(os.path.dirname(__file__)), filename)


try:
    with open(input_file_path, 'r') as f:
        lines = [line.strip() for line in f]

except Exception as e:
    sys.exit("Error - while reading input file: %s" % e)




# Computing frequency reached twice
total = 0
reachedTwice = False
frequencyDict = {0: 1} # 0 was already reached

while (not reachedTwice):

    for num in lines:
        num = int(num)
        total += num

        if total in frequencyDict:
            reachedTwice = total
            break

        else:
            frequencyDict[total] = 1


if reachedTwice:
    print("First frequency reached twice is: %d" % reachedTwice)
else:
    print("No frequency was reached twice")
