from math import sqrt
t = int(input())


def get_factors(x):
    factors = [1]
    for i in range(2, int(sqrt(x)) + 1):
        if k % i == 0:
            factors.append(i)
    factors.append(x)
    return factors


for _ in range(t):
    n, k = list([int(x) for x in input().split()])
    a = list([int(x) for x in input().split()])
    factors = get_factors(k)
    total = 0
    for factor in factors:
        if factor > len(a):
            break
        freq = {}
        sliding_window = a[0:factor]
        s = sum(sliding_window)
        freq[s] = 1
        for i in range(factor, len(a)):
            sliding_window = sliding_window[1:] + [a[i]]

            s = sum(sliding_window)
            if s > k / factor:
                continue
            if s not in freq:
                freq[s] = 0
            freq[s] += 1
        for s in freq:
            total += freq.get((k // factor) - s, 0) * freq[s]
    print(total)
