
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    start = 0
    while start < len(a) and a[start] == 0:
        start += 1
    end = n - 1
    while end >= 0 and a[end] == 0:
        end -= 1
    best = max(1, end - start + 1)
    print(best)
