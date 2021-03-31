#!/usr/bin/python
import sys

# group level master info
current_vin = None
current_values = []
# to store make, model, year values stored with 'I' incident types
car_dict = {}


def reset():
    """
    Resets master info for every new group

    Returns
    -------
    None
    """
    global current_vin
    global current_values
    global car_dict
    current_vin = None
    current_values = []
    car_dict = {}


def flush():
    """
    Filters for incident type 'A' and prints VIN, incident type, make, and year for end of every group

    Returns
    -------
    None
    """
    global current_vin
    global current_values
    global car_dict
    for value in current_values:
        incident_filter = value[0]
        if incident_filter == "A":
            make = car_dict[current_vin][1]
            year = car_dict[current_vin][2]
            new_value = (incident_filter, make, year)
            print(f"{current_vin}\t{new_value}")
            # print '%s\t%s' % (current_vin, new_value)
        else:
            continue


for line in sys.stdin:
    row_data = line.split("\t")
    vin = row_data[0]
    tuple_values = eval(row_data[1])
    incident_type = tuple_values[0]
    if incident_type == "I":
        car_dict[vin] = tuple_values

    # detect key changes
    if current_vin != vin:
        if current_vin is not None:
            flush()
        reset()
    # update master info after key change handling
    current_values.append(tuple_values)
    current_vin = vin
flush()
