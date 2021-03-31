#!/usr/bin/python
import sys

for line in sys.stdin:
    row_data = line.split(",")
    vin_number = row_data[2]
    # incident type, make, year
    values = (row_data[1], row_data[3], row_data[5])
    print(f"{vin_number}\t{values}")
    # print '%s\t%s' % (vin_number, values)
