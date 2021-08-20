t = int(input())
while t > 0:
    (a, b) = map(int, input().split())
    l = list(map(int, input().split()))
    if max(l) - min(l) < b:
        print('YES')
    else:
        print('NO')
    t -= 1
