from itertools import permutations
from sys import stdin


def checkit(vector, upto=-1):
    if upto == -1:
        upto = len(vector)
    for i in range(0, upto):
        if vector[vector[i] - 1] != len(vector) - (i + 1) + 1:
            return False
    return True


def calculate(n):
    numbers = list(range(1, n + 1))
    result = [0] * n
    for i in range(0, n):
        if result[i] != 0:
            continue
        if i > 0 and checkit(result, i):
            continue

        expected = n - i

        for v in numbers:
            if v - 1 == i and expected != v:
                continue

            if v == expected:
                result[v - 1] = v
                numbers.remove(v)
                break
            elif result[v - 1] == expected:
                numbers.remove(v)
                result[i] = v
                break
            elif result[v - 1] == 0:
                assert expected in numbers
                result[i] = v
                result[v - 1] = expected
                numbers.remove(v)
                numbers.remove(expected)
                break

    return result


def calculate_v2(n):
    result = [0] * n
    first_sum = n + 2
    second_sum = n

    nf = n
    i = 0
    while nf > first_sum // 2:
        result[i] = first_sum - nf
        result[i + 1] = nf
        nf -= 2
        i += 2

    if n % 2 == 1:
        result[i] = i + 1

    i = n - 1
    while i > n // 2:
        result[i] = i
        result[i - 1] = second_sum - i
        i -= 2

    return result


def main():
    number = int(stdin.readline())
    result = calculate_v2(number)
    if not checkit(result):
        print(-1)
    else:
        print(" ".join([str(v) for v in result]))


def __starting_point():
    main()


__starting_point()
