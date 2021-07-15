def count_ways(n, k):
    steps = [1] * (n + 1)
    for i in range(1, n + 1):
        if i <= k:
            steps[i] = sum(steps[j] for j in range(0, i))
        else:
            steps[i] = sum(steps[i - j] for j in range(1, k + 1))
    return steps[-1]

