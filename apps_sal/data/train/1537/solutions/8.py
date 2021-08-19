import math


def isPrime(nm):
    for i in range(2, int(math.sqrt(nm) + 1)):
        if nm % i == 0:
            return False
    return True


U = list()
num = 2
for i in range(10000):
    while not isPrime(num):
        num += 1
    U.append(num)
    num += 1
S = list()
for i in range(1, len(U)):
    if isPrime(i + 1):
        S.append(U[i])
t = int(input())
for i in range(t):
    sum = 0
    n = int(input())
    for j in range(n):
        sum += S[j]
    print(sum)
