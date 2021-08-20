import math


def isPrime(n):
    checkNum = int(math.sqrt(n))
    for i in range(1, checkNum + 1):
        if n % i == 0 and i != 1:
            return False
    return True


def backwardsPrime(start, stop):
    backwardsPrimes = []
    for i in range(start, stop + 1):
        if isPrime(i) == True:
            reversedPrime = int(str(i)[::-1])
            if isPrime(reversedPrime) and reversedPrime != i:
                backwardsPrimes.append(i)
    return backwardsPrimes
