from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    sum_of_primes = 0
    if n < 2:
        pass
    elif n == 2:
        sum_of_primes = 2
    else:
        sum_of_primes = 2
        for number in range(3, n + 1, 2):
            for odd in range(3, int(sqrt(number)) + 1, 2):
                if (number % odd) == 0:
                    break
            else:
                sum_of_primes += number
    print(sum_of_primes)
