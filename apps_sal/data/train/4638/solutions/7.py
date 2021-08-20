def fizz_buzz_cuckoo_clock(time):
    (h, m) = list(map(int, time.split(':')))
    if m == 0:
        return ' '.join(['Cuckoo'] * ((h - 1) % 12 + 1))
    elif m == 30:
        return 'Cuckoo'
    elif m % 15 == 0:
        return 'Fizz Buzz'
    elif m % 3 == 0:
        return 'Fizz'
    elif m % 5 == 0:
        return 'Buzz'
    else:
        return 'tick'
