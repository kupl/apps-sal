from itertools import count


def layers(n):
    for i in count(1):
        if n <= (2 * i - 1) ** 2:
            return i
