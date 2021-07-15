from math import factorial

def sum_arrangements(num):

    snum = str(num)
    leng = len(snum)
    total = 0
    c = factorial(leng - 1) * sum(map(int, snum))

    for i in range(leng):
        total += c
        c *= 10

    return total
