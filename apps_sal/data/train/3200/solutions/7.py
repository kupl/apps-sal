from itertools import cycle
def thirt(n):
    while True:
        pattern = cycle((1, 10, 9, 12, 3, 4))
        total = sum(int(a) * next(pattern) for a in reversed(str(n)))
        if total == n:
            return total
        n = total
