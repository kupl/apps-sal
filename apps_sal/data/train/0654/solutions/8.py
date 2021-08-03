
for _ in range(int(input())):
    n = list(map(int, input().split()))
    l = len(n)
    a = sorted(n)
    print(a[l - 2])
