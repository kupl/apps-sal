def fizz_buzz_cuckoo_clock(time):
    h, m = map(int, time.split(':'))
    
    # on the hour
    if m == 0:
        h = h if h in range(1, 13) else abs(h - 12)
        return ('Cuckoo ' * h).rstrip()
    
    # on the half hour
    if m == 30:
        return 'Cuckoo'
    
    # % 3 and 5
    if m % 3 == 0 and m % 5 == 0:
        return 'Fizz Buzz'
    
    # % 3
    if int(m) % 3 == 0:
        return 'Fizz'
    
    # % 5
    if m % 5 == 0:
        return 'Buzz'
    
    # else
    return 'tick'
