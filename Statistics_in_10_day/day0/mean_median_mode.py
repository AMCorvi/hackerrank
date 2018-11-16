import math

# Retrieve the quantity of expected values
# amount_of_values = int(input())
# Retrieve the values themselves as an
# array of integers

# values = [int(val) for val in input().split()]
# amount_of_values = len(values)
values = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060".split()
values = [int(value) for value in values]
amount_of_values = len(values)


def mean(quant_of_vals, values):

    sum_of_values = 0
    # obtain sum of values provided
    for val in values:
        sum_of_values = sum_of_values + val

    # divide sum of all values by the quantity values
    mean = sum_of_values / quant_of_vals
    return round(mean, 1)


def median(quant_of_vals, values):
    center = {}
    # determine the 'middle-most' values or value
    if quant_of_vals % 2 == 0:
        # determin center of the values ( which will be decimal)
        # and collect result of rounding down and up as the
        # first and second center values respectively.
        values = sorted(values)
        mid_val = math.floor(quant_of_vals / 2)
        center["one"] = values[mid_val]
        center["two"] = values[mid_val - 1]
        return round(((center["one"] + center["two"]) / 2), 2)
    else:
        return round(values[math.ceil(quant_of_vals) - 1], 2)


def mode(values):
    # create dictionary whcih will contain freq data
    freq = {}

    # stratify names into dictionary with values of fields
    # being frequency of occurences
    for val in values:
        # if value already exists in the dictionary
        # add one addtional instance to the that value
        if val in freq:
            freq[val] += 1
        # else create value in the dictionary indicating
        # it single instance
        else:
            freq[val] = 1

    # sort frequencies in ascending order
    freq = sorted(freq.items())
    # set smallest value as the result. If any proceeding
    # value has a higher frequency set that val as the
    # new result and repeat until the array is exhausted

    mode = None
    for val in freq:
        freq_of_current_val = val[1]
        # Branches
        if mode == None:
            # No value set to mode
            mode = val
            continue
        elif freq_of_current_val < mode[1]:
            # Value not greater
            continue
        elif freq_of_current_val > mode[1]:
            # Value is greater
            mode = val
    return mode[0]


print(mean(amount_of_values, values))
print(median(amount_of_values, values))
print(mode(values))
