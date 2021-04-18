#!/usr/bin/python
import sys

# group level master info
current_vin = None
make = None
year = None
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
    global make
    global year
    current_vin = None
    current_values = []
    make = None
    year = None


def flush():
    """
    Filters for incident type 'A' and prints VIN, incident type, make, and year for end of every group

    Returns
    -------
    None
    """
    for value in current_values:
        incident_filter = value[0]
        if incident_filter == "A":
            new_value = (incident_filter, make, year)
            print(f"{current_vin}\t{new_value}")
            # print '{0}\t{1}' % (current_vin, new_value)
        else:
            continue


for line in sys.stdin:
    line = line.strip()
    row_data = line.split("\t")
    vin = row_data[0]
    tuple_values = eval(row_data[1])
    incident_type = tuple_values[0]

    # detect key changes
    if current_vin != vin:
        if current_vin is not None:
            flush()
        reset()
    if incident_type == "I":
        make = tuple_values[1]
        year = tuple_values[2]

    # update master info after key change handling
    current_values.append(tuple_values)
    current_vin = vin
flush()
