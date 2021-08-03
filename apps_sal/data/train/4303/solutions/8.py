def sum_arrangements(num):
    s = str(num)
    from math import factorial
    return factorial(len(s) - 1) * int("1" * len(s)) * sum(int(i) for i in s)
