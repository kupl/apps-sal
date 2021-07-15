for _ in range(int(input())):
    n = int(input())
    a = list(map('12'.__contains__, input().strip()))
    b = list(map('12'.__contains__, input().strip()))
    u, d = True, False
    for i in range(n):
        if a[i]:
            if not b[i]:
                d = False
        else:
            if b[i]:
                u = False
            else:
                u, d = d, u
        if not (u or d):
            break
    print('YES' if d else 'NO')

