import re


def get_sum_of_digits(num):
    sum = 0
    num = str(num)
    digits = re.findall("[0-9]{1}", num)
    for x in digits:
        x = int(x)
        sum = sum + x
    return sum
