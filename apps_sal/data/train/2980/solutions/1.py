from collections import Counter


def number_of_div(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    mu = 1
    # print(factors)
    po = [i + 1 for i in list(Counter(factors).values())]
    for i in po:
        mu *= i
    return mu


def find_min_num(num_div):
    for i in range(1, num_div**4):
        num = number_of_div(i)
        if num == num_div:
            return i
