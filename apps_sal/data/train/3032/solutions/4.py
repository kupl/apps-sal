LIMIT = 351
memo = [[] for _ in range(LIMIT)]
for x in range(2, LIMIT):
    if not memo[x]:
        memo[x] = ['None']
    for y in range(2 * x, LIMIT, x):
        memo[y].append(x)


def factorsRange(n, m):
    return {i: memo[i] for i in range(n, m + 1)}
