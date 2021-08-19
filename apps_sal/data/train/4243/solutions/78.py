def find_average(values):
    sum_of_values = 0
    i = 0
    for value in values:
        i += 1
        sum_of_values += value
    return sum_of_values / i
