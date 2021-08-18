def fizz_buzz_cuckoo_clock(time):
    h, m = map(int, time.split(':'))

    if m == 0:
        h = h if h in range(1, 13) else abs(h - 12)
        return ('Cuckoo ' * h).rstrip()

    if m == 30:
        return 'Cuckoo'

    if m % 3 == 0 and m % 5 == 0:
        return 'Fizz Buzz'

    if int(m) % 3 == 0:
        return 'Fizz'

    if m % 5 == 0:
        return 'Buzz'

    return 'tick'
