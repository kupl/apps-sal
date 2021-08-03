# https://www.geeksforgeeks.org/largest-odd-divisor-game-to-check-which-player-wins/
from sys import stdin, stdout


def winner(n, k):
    cnt = 0
    if (n == 1):
        print("Grinch")
    elif ((n & 1) or n == 2):
        print("Me")
    else:
        tmp = n
        val = 1
        while (tmp > k and tmp % 2 == 0):
            tmp //= 2
            val *= 2
        for i in range(3, int(tmp**0.5) + 1):
            while (tmp % i == 0):
                cnt += 1
                tmp //= i
        if (tmp > 1):
            cnt += 1
        if (val == n):
            print("Grinch")
        elif (n / tmp == 2 and cnt == 1):
            print("Grinch")
        else:
            print("Me")


test = int(stdin.readline())
for _ in range(test):
    n = int(stdin.readline())
    winner(n, 1)
