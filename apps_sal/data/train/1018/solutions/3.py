# 872//2
for _ in range(int(input())):
    n, a, b = int(input()), list(map(int, input().split())), []
    for i in range(n - 1):
        b.append(a[i] - a[i + 1])
    print(min(b))
