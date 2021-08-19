from math import sqrt
t = int(input())
while t:
    t -= 1
    n = int(input())
    if n == 1:
        print('Grinch')
    elif n & 1 or n == 2:
        print('Me')
    else:
        cnt = 0
        tmp = n
        val = 1
        while tmp > 1 and tmp % 2 == 0:
            tmp //= 2
            val *= 2
        for i in range(3, int(sqrt(tmp)) + 1):
            while tmp % i == 0:
                cnt += 1
                tmp //= i
        if tmp > 1:
            cnt += 1
        if val == n:
            print('Grinch')
        elif n / tmp == 2 and cnt == 1:
            print('Grinch')
        else:
            print('Me')
