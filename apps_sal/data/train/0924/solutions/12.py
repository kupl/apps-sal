import math


def distinctPrimeFactors(num):
    primes = set()

    if (num == 2):
        primes.add(num)

    sqrt = int(math.sqrt(num))
    for j in range(2, sqrt + 1):
        if (num % j == 0):
            primes.add(j)
            while (num % j == 0):
                num //= j
    if (num > 2):
        primes.add(num)

    return (primes)


res = []
c = 0
lst = {}
primes = {}
rangeData = {}
k, q = map(int, input().split())
primes[k] = distinctPrimeFactors(k)
for tc in range(q):
    query = input()
    if (query[0] == '!'):
        cmd, l, r, x = query.split()
        l = int(l)
        r = int(r)
        x = int(x)
        start = l
        end = r
        startflag = False
        for i in sorted(rangeData):
            rangeVal = i

            if (start > rangeVal[1]):
                continue
            if (end < rangeVal[0]):
                break

            startRange = start
            endRange = end
            if (start >= rangeVal[0] and start <= rangeVal[1]):
                start = rangeVal[1] + 1
                continue
            if (end >= rangeVal[0]):
                endRange = rangeVal[0] - 1
            if (startRange <= endRange):
                rangeData[(startRange, endRange)] = x
                start = max(endRange + 1, rangeVal[1] + 1)
        if (start <= end):
            rangeData[(start, end)] = x
    elif (query[0] == '?'):
        cmd, l, r = query.split()
        l = int(l)
        r = int(r)
        count = 0
        for primenum in primes[k]:
            for currRange in rangeData:
                if (not (r < currRange[0] or l > currRange[1])):
                    num = rangeData[currRange]
                    if (num % primenum == 0):
                        count += 1
                        break
        c += 1
        res.append(count)

for i in range(c):
    print(res[i])
