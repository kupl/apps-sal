t = int(input())
for i in range(t):
    n = int(input())
    a = []
    a = list(map(int, input().split()))
    a = sorted(a)
    diff = []
    for i in range(n - 1):
        diff.append(a[i + 1] - a[i])
    print(min(diff))
