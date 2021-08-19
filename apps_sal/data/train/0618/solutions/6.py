inp = list(map(int, input().split()))
t = inp[0]
for te in range(t):
    inp = list(map(int, input().split()))
    n = inp[0]
    k = inp[1]
    inp = list(map(int, input().split()))
    max = 0
    for i in range(k):
        max = max + inp[i % n]
        sums = max
    for j in range(0, n):
        sums = sums - inp[j] + inp[(j + k) % n]
        if sums > max:
            max = sums
    print(max)
