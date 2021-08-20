from math import sqrt


def consecutive_sum(num):
    counter = 1
    for i in range(2, int(sqrt(2 * num) + 1)):
        if i % 2 == 0:
            if num / i - num // i == 0.5:
                counter += 1
        elif num / i == num // i:
            counter += 1
    return counter
