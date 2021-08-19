try:
    t = int(input())
    for i in range(t):
        (a, b, c) = map(int, input().split(' '))
        if a > 0 and b > 0 and (c > 0):
            if a >= b and a >= c:
                if a ** 2 == b ** 2 + c ** 2:
                    print('YES')
                else:
                    print('NO')
            elif b >= a and b >= c:
                if b ** 2 == a ** 2 + c ** 2:
                    print('YES')
                else:
                    print('NO')
            elif c ** 2 == a ** 2 + b ** 2:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
except:
    pass
