n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if a[2] <= a[1] + a[0] + 1:
        print('Yes')
    else:
        print('No')
