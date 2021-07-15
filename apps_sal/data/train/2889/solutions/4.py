def count_ways(n, k):
    kfib = [0 for _ in range(k-1)] + [1]
    for i in range(n):
        kfib.append(sum(kfib[i:i+k]))
    return kfib[-1]
