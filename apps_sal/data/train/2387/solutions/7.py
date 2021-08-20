import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    ANS = 0
    while n >= 10:
        back = n // 10
        buy = back * 10
        ANS += buy
        n -= buy
        n += back
    print(ANS + n)
