t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    l1 = list(map(int, (input().split())))
    l1.sort()
    diff = l1[-1] - l1[0]
    if k < diff:
        print('NO')
    else:
        print('YES')
