def fizz_buzz_cuckoo_clock(t):
    (h, m) = list(map(int, t.split(':')))
    h = h - 12 if h > 12 else h + 12 if h == 0 else h
    if m == 0:
        return ' '.join(('Cuckoo' for i in range(h)))
    if m == 30:
        return 'Cuckoo'
    if m % 3 == 0 and m % 5 == 0:
        return 'Fizz Buzz'
    if m % 3 == 0:
        return 'Fizz'
    if m % 5 == 0:
        return 'Buzz'
    return 'tick'
