n = int(input())
for _ in range(n):
    k = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[k - 1] * a[k - 2], a[0] * a[1])
