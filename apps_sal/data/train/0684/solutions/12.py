import math


def findWinner(n, k):
    cnt = 0
    if n == 1:
        print('Grinch')
    elif n & 1 or n == 2:
        print('Me')
    else:
        tmp = n
        val = 1
        while tmp > k and tmp % 2 == 0:
            tmp //= 2
            val *= 2
        for i in range(3, int(math.sqrt(tmp)) + 1):
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


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        findWinner(n, 1)


__starting_point()
