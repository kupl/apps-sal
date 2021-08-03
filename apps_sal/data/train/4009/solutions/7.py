import math


def convert_to_list(number):
    lst = []
    while number != 0:
        lst.append(number % 10)
        number = int(number / 10)
    return lst


def list_to_list(lst):
    average_list = []
    for i in range(len(lst) - 1):
        average_list.append(math.ceil((lst[i] + lst[i + 1]) / 2))
    return average_list


def digits_average(digits):
    lst = convert_to_list(digits)
    while len(lst) > 1:
        lst = list_to_list(lst)
    return lst[0]
