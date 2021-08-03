from collections import Counter


def get_factors(num):
    if num % 2 == 0:
        return (2, num // 2)
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return (i, num // i)
    return (num, None)


def string_builder(count_dict):
    s = ""
    for element in count_dict:
        if count_dict[element] == 1:
            s += f"({element})"
        else:
            s += f"({element}**{count_dict[element]})"
    return s


def primeFactors(n):
    factors = [n]
    count_dict = Counter()

    while factors:
        result = get_factors(factors.pop())
        count_dict[result[0]] += 1
        if result[1]:
            factors.append(result[1])

    return string_builder(count_dict)
