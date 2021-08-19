from sys import stdin
readline = stdin.readline
results = []
for _ in range(int(readline())):
    (n, d) = list(map(int, readline().split()))
    c = sorted(map(int, readline().split()))
    (low, high) = (0.0, 2000000000.0)
    while low + 1e-06 < high:
        mid = 0.5 * (low + high)
        (elapsed, okay) = (0.0, True)
        for start in c:
            if elapsed > start + d:
                okay = False
                break
            if elapsed < start:
                elapsed = start
            elapsed += mid
        if okay:
            low = mid
        else:
            high = mid
    results.append('{:.6f}'.format(low))
print('\n'.join(results))
