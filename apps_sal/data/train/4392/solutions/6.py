from collections import Counter


def find_lowest_int(k):
    n = 9
    while True:
        if Counter(str(k * n)) == Counter(str((k + 1) * n)):
            return n
        n += 9
