n = int(input())
while n > 0:
    n = n - 1
    lst = []
    (P, X) = map(int, input().split())
    lst = list(map(int, input().split()))
    d = max(lst) - min(lst)
    if d < X:
        print('YES')
    else:
        print('NO')
