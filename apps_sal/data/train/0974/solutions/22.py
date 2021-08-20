t = int(input())
for i in range(t):
    (a, b, c, d) = map(int, input().split())
    if abs(c - d) == 0:
        if a == b:
            print('YES')
        else:
            print('NO')
    elif abs(a - b) % abs(c - d) == 0:
        print('YES')
    else:
        print('NO')
