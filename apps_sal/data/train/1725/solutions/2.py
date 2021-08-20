class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def linear_limited_sums(X, Y, head, tail):
    if X == 1:
        return 1 if head == tail else 0
    if X == 2:
        return 1 if head + tail <= Y else 0
    return sum((linear_limited_sums(X - 1, Y, head, T) for T in range(Y - tail + 1))) % 12345787


def circular_limited_sums(X, Y):
    return sum((linear_limited_sums(X, Y, head, tail) for head in range(Y + 1) for tail in range(Y - head + 1))) % 12345787
