import math


def primeFactors(number):

    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))

    distinct_set = sorted(set(prime_factors))

    output = ""

    for i in distinct_set:

        if(prime_factors.count(i) == 1):

            output = output + '(' + str(i) + ')'
        else:
            output = output + '(' + str(i) + '**' + str(prime_factors.count(i)) + ')'

    return output
