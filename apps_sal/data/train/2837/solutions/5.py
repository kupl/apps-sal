def what_is_the_time(time):
    (h, m) = (int(n) for n in time.split(':'))
    return f'{-(h + (m > 0)) % 12 or 12:02d}:{-m % 60:02d}'
