def count_ways(n, k):
    ways = [None] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in range(1, k + 1):
            if i - j >= 0:
                total += ways[i - j]
        ways[i] = total
    return ways[n]
