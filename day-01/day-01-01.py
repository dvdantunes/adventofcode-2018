#!/usr/bin/python

''' Advent of code - Day 1: Chronal Calibration - Problem 1.1

https://adventofcode.com/2018/day/1
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




# Computing frequency
total = 0
for num in lines:
    num = int(num)
    total += num

print("Total frequency: %d" % total)
