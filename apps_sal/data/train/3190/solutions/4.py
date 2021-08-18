two_digit_primes = set('11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97'.split())

numbers = []
for n in range(11, 9799 + 1):
    if str(n)[:2] in two_digit_primes:
        for ending in (0, 1, 25, 76):
            candidate = n * 100 + ending
            if str(candidate**2)[:2] in two_digit_primes:
                numbers.append(candidate)


def solve(a, b):
    return sum(1 for n in numbers if a <= n < b)
