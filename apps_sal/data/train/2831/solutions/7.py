import math

def largest_pair_sum(numbers):
    a, b = -math.inf, -math.inf
    for n in numbers:
        if n > a:
            if a > b:
                b = a
            a = n
        elif n > b:
            b = n
    return a + b
