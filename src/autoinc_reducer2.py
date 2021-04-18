#!/usr/bin/python
import sys

# group level master info
current_vin = None
current_values = []


def reset():
    """
    Resets master info for every new group

    Returns
    -------
    None
    """
    global current_vin
    global current_values
    current_vin = None
    current_values = []


def flush():
    """
    Prints concatenated make and year & count for each group

    Returns
    -------
    None
    """
    total = 0
    for value in current_values:
        total += value
    print(f"{current_vin}\t{total}")
    # print '{0}\t{1}'.format(current_vin, total)


for line in sys.stdin:
    row_data = line.split("\t")
    vin = row_data[0]
    count_value = int(row_data[1])

    # detect key changes
    if current_vin != vin:
        if current_vin is not None:
            flush()
        reset()

    # update master info after key change handling
    current_values.append(count_value)
    current_vin = vin
flush()
