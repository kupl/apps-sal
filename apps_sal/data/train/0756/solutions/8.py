import math


def isPrime(n):
    flag = 0
    for j in range(2, int(n)):
        if n % j == 0:
            flag = 0
            break
        flag = 1
    return flag


for i in range(int(input())):
    ip = list(map(int, input().split()))
    pots = sum(ip)
    flag = 0
    cnt = 1
    while True:
        if isPrime(pots + cnt) == 1:
            print(cnt)
            break
        else:
            cnt += 1
