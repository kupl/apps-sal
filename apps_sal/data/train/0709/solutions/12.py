t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] > a[n - 1]:
        print(a[0])
    else:
        print(a[n - 1])
