def find_factors(n):
    factors = []
    for i in (7, 5, 3, 2):
        while n % i == 0:
            n = n / i
            factors.append(i)
    if n > 0:
        return factors + [n]
    return factors


def is_smooth(n):
    f = {2: 'power of 2', 3: '3-smooth', 5: 'Hamming number', 7: 'humble number'}
    return f.get(max(find_factors(n)), 'non-smooth')
