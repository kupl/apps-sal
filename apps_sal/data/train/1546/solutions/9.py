T = int(input())
while T > 0:
    (a, b, c) = [int(x) for x in input().split()]
    if a + b > c and b + c > a and (c + a > b):
        if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    T -= 1
