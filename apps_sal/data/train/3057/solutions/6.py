def is_bouncy(number):
    n = str(number)
    s = ''.join(sorted(n))
    return s != n != s[::-1]

