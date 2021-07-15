from collections import defaultdict


names = defaultdict(lambda: 'non-smooth', {
    2: 'power of 2',
    3: '3-smooth',
    5: 'Hamming number',
    7: 'humble number',
})


def is_smooth(n):
    divisors = set()
    for d in [2, 3, 5, 7]:
        while n % d == 0:
            divisors.add(d)
            n //= d
    if n != 1:
        divisors.add(9)
    return names[max(divisors, default=9)]
