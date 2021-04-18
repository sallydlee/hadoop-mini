#!/usr/bin/python
import sys

for line in sys.stdin:
    row_data = line.split("\t")
    vin_number = row_data[0]
    tuple_values = eval(row_data[1])
    # key is concat of vehicle make and year
    make_year = f"{tuple_values[1]}{tuple_values[2]}"
    print(f"{make_year}\t{1}")

    # make_year = '{0}{1}'.format(tuple_values[1], tuple_values[2])
    # print '{0}\t{1}'.format(make_year, 1)

