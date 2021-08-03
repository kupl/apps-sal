memo = [2, 1]


def lucasnum(n):
    m = abs(n)
    while len(memo) < m + 1:
        memo.append(memo[-1] + memo[-2])
    return memo[m] * (-1)**(n < 0 and n % 2)
