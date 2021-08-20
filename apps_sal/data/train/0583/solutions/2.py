for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    (a, b) = (0, 0)
    if n == 1:
        if l[0] >= 0:
            print('YES')
        else:
            print('NO')
    else:
        for i in l:
            if i < 0:
                b += i
            else:
                a += i
        if a >= abs(b):
            print('YES')
        else:
            print('NO')
