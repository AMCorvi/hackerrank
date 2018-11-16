from functools import reduce
quantity_of_datapoints = int(input())
values = [int(value) for value in input().split()]
weights = [int(weight) for weight in input().split()]
quantity_of_datapoints = len(values) if len(weights) == len(
    values) else quantity_of_datapoints

# quantity_of_datapoints = int(5)
# values = [int(value) for value in "10 40 30 50 20 ".split()]
# weights = [int(weight) for weight in "1 2 3 4 5".split()]
# quantity_of_datapoints = len(values) if len(weights) == len(
#     values) else quantity_of_datapoints


def weighted_mean(quant, ws, vs):
    # calculate the weighted sum (numerator) of mean formula
    weighted_sum = reduce(
        # mulitply the value by the weight of the data index
        lambda sum, index: (vs[index] * ws[index]) + sum,
        range(quant),
        0)

    # calculate the total weight
    total_weight = reduce(lambda sum, weight: weight + sum, ws, 0)

    # divide weighted_sum by totat_weight
    weighted_mean = (weighted_sum / total_weight)

    # constrain return value to the tenths place
    return round(weighted_mean, 1)


print(weighted_mean(quantity_of_datapoints, weights, values))
