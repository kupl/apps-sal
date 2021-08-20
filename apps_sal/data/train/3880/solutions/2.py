def is_smooth(n):
    for v in [2, 3, 5, 7]:
        while n % v == 0:
            n /= v
        if n == 1:
            return ['', '', 'power of 2', '3-smooth', '', 'Hamming number', '', 'humble number'][v]
    return 'non-smooth'
