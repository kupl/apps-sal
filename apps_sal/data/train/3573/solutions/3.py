def score(a, b, c):
    if a + b < c:
        return a + b
    return (a + b - c) // 2 + c


def solve(arr):
    (a, b, c) = arr
    return min(score(a, b, c), score(b, c, a), score(c, a, b))
