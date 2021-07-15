t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(max(a[0], a[n - 1]))
