t = int(input())
for _ in range(t):
    (m, t1, t2) = map(int, input().split())
    x = abs(t1 - t2)
    if x % 3 == 0 and x // 3 <= m:
        print('No')
    else:
        print('Yes')
