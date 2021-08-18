t = int(input())
while(t):
    n = int(input())
    k = int(input())
    if max(n, k) % min(n, k) == 0:
        print('YES')
    else:
        print('NO')
    t -= 1
