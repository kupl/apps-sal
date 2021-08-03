import math


def store_diviors_squared_sum(func):
    store = {}

    def helper(integer):
        if integer not in store:
            store[integer] = func(integer)
        return store[integer]
    return helper


@store_diviors_squared_sum
def divisors_squared_sum(integer):
    squared_divisors_sum = 1
    for number in range(2, integer + 1):
        if integer % number == 0:
            squared_divisors_sum += number**2
    return squared_divisors_sum


def list_squared(m, n):
    return_array = []
    for integer in range(m, n + 1):
        squared_divisors_sum = divisors_squared_sum(integer)
        if math.sqrt(squared_divisors_sum) % 1 == 0:
            return_array.append([integer, squared_divisors_sum])
    return return_array
