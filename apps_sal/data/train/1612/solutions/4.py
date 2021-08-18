import math
from collections import Counter
from itertools import permutations


def find_spec_prod_part(n, com):
    temp_partition = []
    factors = primeFactors(n)
    counter = Counter(factors)
    max_score = calculateScore(counter)
    min_score = max_score
    partition_min = factors
    partition_max = factors

    x = len(factors)

    if len(factors) == 1:
        return "It is a prime number"

    perms = list(set(list(permutations(factors))))

    divs = list(accel_asc(len(factors)))

    for div in divs:
        if len(div) == 1 or len(div) == len(factors):
            continue
        for perm in perms:
            temp_partition = []
            start = 0
            product = 1
            seq = []

            for i in div:
                seq = perm[start:(start + i)]
                for j in seq:
                    product *= j
                temp_partition.append(product)
                start = start + i
                product = 1

            counter = Counter(temp_partition)
            score = calculateScore(counter)

            if score > max_score:
                max_score = score
                partition_max = temp_partition

            if score < min_score:
                min_score = score
                partition_min = temp_partition

    if com == 'max':
        partition_max.sort(reverse=True)
        return [partition_max, max_score]
    if com == 'min':
        partition_min.sort(reverse=True)
        return [partition_min, min_score]


def calculateScore(count):
    score = 0
    coef = 0
    for key in count:
        score += key**count[key]
        coef += count[key]
    score = score * coef
    return score


def primeFactors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            prime_factors.append(i),
            n = n / i
    if n != 1:
        prime_factors.append(int(n))

    return prime_factors


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]
