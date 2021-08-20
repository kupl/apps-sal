t = int(input())
for i in range(t):
    (a, b, c, d) = list(map(int, input().split()))
    if c == d:
        if a == b:
            print('YES')
        else:
            print('NO')
    elif abs(a - b) % abs(c - d) == 0:
        print('YES')
    else:
        print('NO')
