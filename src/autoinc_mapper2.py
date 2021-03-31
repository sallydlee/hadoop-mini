#!/usr/bin/python
import sys

for line in sys.stdin:
    row_data = line.split("\t")
    vin_number = row_data[0]
    tuple_values = eval(row_data[1])
    # key is concat of vehicle make and year
    make_year = f"{tuple_values[1]}{tuple_values[2]}"
    print(f"{make_year}\t{1}")
    # print '%s\t1' % (make_year)
