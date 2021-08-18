import math
for i in range(int(input())):
    x, y = map(int, input().split())
    sumi = x + y

    def isPrime(n):
        if(n <= 1):
            return False
        if(n <= 3):
            return True
        if(n % 2 == 0 or n % 3 == 0):
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0):
                return False
        return True

    def nextPrime(N):
        if (N <= 1):
            return 2

        prime = N
        found = False

        while(not found):
            prime = prime + 1

            if(isPrime(prime) == True):
                found = True

        return prime

    print(nextPrime(sumi) - sumi)
