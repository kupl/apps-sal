import math


def gen_primes(num):
    nonlocal primes
    flag = False
    j = 0
    for i in range(primes[-1] + 1, num + 1):
        while primes[j] <= math.sqrt(i):
            if i % primes[j] == 0:
                flag = True
                break
            j += 1
        if flag:
            flag = False
            pass
        else:
            primes.append(i)


def divisible(num):
    nonlocal primes, d, divisors
    srt = int(round(math.sqrt(num)))
    if srt <= primes[-1]:
        for i in primes:
            if num % (i * i) == 0:
                d = i
                return True
            elif num % i == 0:
                if divisors.get(i, 0):
                    d = i
                    return True
                else:
                    divisors[i] = 1

    else:
        gen_primes(srt)
        for i in primes:
            if num % (i * i) == 0:
                d = i
                return True
            elif num % i == 0:
                if divisors.get(i, 0):
                    d = i
                    return True
                else:
                    divisors[i] = 1


primes = [2, 3, 5, 7, 11]
for i in range(eval(input())):
    n = eval(input())
    l = input().strip().split()
    divisors = {}
    d = 0
    for j in range(n):
        l[j] = int(l[j])
        check = divisible(l[j])
        if check:
            print(d)
            break
