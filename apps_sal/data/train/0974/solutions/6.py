n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    a = min(l[0], l[1])
    b = max(l[0], l[1])
    c = min(l[2], l[3])
    d = max(l[2], l[3])
    if d != c:
        d = d - c
        t = (b - a) // d
        a = a + t * d
        if a == b:
            print('YES')
        else:
            print('NO')
    elif a != b:
        print('NO')
    else:
        print('YES')
