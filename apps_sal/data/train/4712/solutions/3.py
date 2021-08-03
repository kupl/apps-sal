memo = {0: 2, 1: 1}
current = [-1, 2]


def lucasnum(n):
    while n not in memo:
        if n < 0:
            x = current[0]
            memo[x] = memo[x + 2] - memo[x + 1]
            current[0] -= 1
        else:
            x = current[1]
            memo[x] = memo[x - 2] + memo[x - 1]
            current[1] += 1
    return memo[n]
