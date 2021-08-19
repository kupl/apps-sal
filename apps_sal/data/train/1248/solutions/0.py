def finder(n):
    cnt = 0
    for i in range(2, n + 1):
        a = n
        while a != 0:
            r = a % i
            a = a // i
        if r == 1:
            cnt += 1
    return cnt


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print('INFINITY')
    else:
        print(finder(n))
