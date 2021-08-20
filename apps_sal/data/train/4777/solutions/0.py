from collections import Counter


def mystery_range(s, n):
    (i, target) = (-1, Counter(s))
    sum_ = sum(map(Counter, map(str, range(n))), Counter())
    while True:
        i += 1
        sum_ = sum_ - Counter(str(i)) + Counter(str(i + n))
        if sum_ == target:
            if len(str(i + 1)) < len(str(i + n)) or str(i + 1) in set(map(''.join, zip(*[iter(s)] * len(str(i + 1))))):
                return [i + 1, i + n]
