def fizz_buzz_cuckoo_clock(time):
    hours, minutes = map(int, time.split(':'))
    hours = hours - 12 * (hours > 12) or 12
    if not minutes % 30:
        return ' '.join(['Cuckoo'] * (hours if not minutes else 1))
    return ' '.join(('Fizz' * (not minutes % 3), 'Buzz' * (not minutes % 5))).strip() or 'tick'
