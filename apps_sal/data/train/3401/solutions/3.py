from functools import reduce


def eq_dice(set_):
    n = reduce(int.__mul__, [s for s in set_ if s not in (11, 13)])
    stack = [[n, [s for s in set_ if s in (11, 13)]]]
    result = set()
    while stack:
        (n, status) = stack.pop()
        if 3 <= n <= 20 and len(status) > 0:
            result.add(tuple(sorted(status + [n])))
        for i in range(3, min(20, int(n // 3)) + 1):
            if n % i == 0 and n // i >= 3:
                stack.append([n // i, sorted(status + [i])])
    result.discard(tuple(sorted(set_)))
    return len(result)
