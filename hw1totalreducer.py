#!/usr/bin/env python
# Outputs just an integer of the total n-gram count.
import sys

sep='\t'
total_count = 0

for line in sys.stdin:
    key, value = line.strip().split(sep)
    total_count += int(value)

print(total_count)