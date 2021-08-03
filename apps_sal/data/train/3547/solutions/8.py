def odd_ones_out(numbers):
    return list(filter(lambda x: not numbers.count(x) % 2, numbers))
