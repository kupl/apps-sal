import functools
# def get_sum_of_digits(num):
#     sum = 0
#     digits = str(num)
#     for x in digits:
#         sum += int(x)
#     return sum


def get_sum_of_digits(num):
    return functools.reduce(lambda a, b: a + b, [int(x) for x in str(num)])
