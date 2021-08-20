def fizz_buzz_cuckoo_clock(time):
    (hh, mm) = map(int, time.split(':'))
    if mm == 0:
        return ' '.join(['Cuckoo'] * (hh % 12 or 12))
    elif mm == 30:
        return 'Cuckoo'
    elif mm % 15 == 0:
        return 'Fizz Buzz'
    elif mm % 3 == 0:
        return 'Fizz'
    elif mm % 5 == 0:
        return 'Buzz'
    else:
        return 'tick'
