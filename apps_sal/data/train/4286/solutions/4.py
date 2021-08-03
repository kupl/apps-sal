from math import sqrt


def solve(n):

    ls = []

    for i in range(n, n + 300):

        temp = True
        for j in range(2, int(sqrt(n)) + 10):

            if i % j == 0 and i != j:
                temp = False
                break
        if temp:
            ls.append(i)
            break

    for i in range(n - abs(n - ls[0]), n + 1):

        temp = True
        for j in range(2, int(sqrt(n)) + 10):

            if i % j == 0 and i != j:
                temp = False
                break
        if temp:
            ls.append(i)

    if len(ls) > 1:
        return ls[-1]
    return ls[0]
