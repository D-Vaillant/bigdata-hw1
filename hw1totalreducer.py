#!/usr/bin/env python
# Outputs just an integer of the total n-gram count.
import sys

sep='\t'
total_count = 0

def read_mapper_output(input, sep='\t'):
    for line in input:
        yield line.rstrip().split(sep, 1)


data = read_mapper_output(sys.stdin, sep=sep)
for line in data:
    total_count += 1

print(f"TotalCount\t{total_count}")
