import sys
input = sys.stdin.buffer.readline

MAXPRIME = 10**6
isPrime = [0 for _ in range(MAXPRIME + 1)]
isPrime[0] = -1
isPrime[1] = -1
for i in range(2, MAXPRIME // 2 + 1):
    if isPrime[i] == 0:
        for multiple in range(i * i, MAXPRIME + 1, i):
            if isPrime[multiple] == 0:
                isPrime[multiple] = i
primeNumberSet = set()
for i in range(len(isPrime)):
    if isPrime[i] == 0:
        primeNumberSet.add(i)
primes = sorted(list(primeNumberSet))

lookupTable = [None for _ in range(MAXPRIME + 1)]

pIdx = -1
pSqRtIdx = -1
for i in range(1, MAXPRIME + 1):
    while pIdx + 1 < len(primes) and primes[pIdx + 1] <= i:
        pIdx += 1
    while pSqRtIdx + 1 < len(primes) and (primes[pSqRtIdx + 1])**2 <= i:
        pSqRtIdx += 1
    total = (pIdx + 1) - (pSqRtIdx + 1) + 1
    lookupTable[i] = total


t = int(input())
n = [int(x) for x in input().split()]
print('\n'.join([str(lookupTable[nn]) for nn in n]))
