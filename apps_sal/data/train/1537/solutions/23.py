def isPrime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                return False
        return True


def getNextPrime(n):
    n = n + 1
    while(not isPrime(n)):
        n += 1
    return n


t = int(input())


for _ in range(t):
    n = int(input())
    sum_ = 0
    currentPrime = 2
    N = 1
    countN = 1
    while countN <= n:
        if isPrime(N):
            sum_ += currentPrime
            countN += 1
        currentPrime = getNextPrime(currentPrime)
        N += 1

    print(sum_ % (1000000000 + 7))
