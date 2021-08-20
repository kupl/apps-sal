def isPrime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def getNextPrime(n):
    n = n + 1
    while not isPrime(n):
        n += 1
    return n


t = int(input())
for _ in range(t):
    n = int(input())
    sum_ = 0
    currentPrime = 3
    N = 2
    countN = 1
    temp = 0
    diff = 0
    while countN <= n:
        sum_ += currentPrime
        countN += 1
        temp = getNextPrime(N)
        diff = temp - N
        for i in range(diff):
            currentPrime = getNextPrime(currentPrime)
        N = temp
    print(sum_ % (1000000000 + 7))
