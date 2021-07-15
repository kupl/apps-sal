def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i) % 2 == 0]
