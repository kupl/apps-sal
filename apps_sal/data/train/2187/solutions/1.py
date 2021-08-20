apples = int(input())
if apples <= 3:
    print(0)
else:
    halfpr = int(apples / 2)

    def primes(n):
        isPrime = [True for i in range(n + 1)]
        isPrime[0] = isPrime[1] = False
        idx = 2
        while idx * idx <= n:
            if isPrime[idx]:
                for i in range(idx * 2, n, idx):
                    isPrime[i] = False
            idx += 1
        return isPrime
    primeslist = primes(halfpr)
    totallist = [False] * (apples + 1)
    applepairs = []
    for prime in range(len(primeslist) - 1, 1, -1):
        if primeslist[prime]:
            numprimes = int(apples / prime)
            primesx = [int(i * prime) for i in range(1, numprimes + 1) if not totallist[i * prime]]
            if len(primesx) % 2 == 1:
                primesx.remove(2 * prime)
            for pr in primesx:
                applepairs.append(pr)
                totallist[pr] = True
    print(int(len(applepairs) / 2))
    for t in range(int(len(applepairs) / 2)):
        print(applepairs[2 * t], applepairs[2 * t + 1])
