memo = {}


def bouncy_ratio(percent):
    if not 0 <= percent <= 0.99:
        raise ValueError
    (b, n) = (0.0, 100)
    while b / n < percent:
        n += 1
        if is_bouncy(n):
            b += 1
    return n


def is_bouncy(n):
    if n in memo:
        return memo[n]
    s = str(n)
    memo[n] = list(s) != sorted(s) and list(s) != sorted(s, reverse=True)
    return memo[n]
