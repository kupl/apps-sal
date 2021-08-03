def memoize(f):
    memo = {}

    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper


@memoize
def sum_of_squares(n):
    squares = [x**2 for x in range(1, n + 1) if n % x == 0]
    return sum(squares)


def list_squared(m, n):
    result = []
    for i in range(m, n):
        sums = sum_of_squares(i)
        if sums > 0 and sums**0.5 % 1 == 0:
            result.append([i, sums])
    return result
