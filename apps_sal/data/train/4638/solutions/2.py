def fizz_buzz_cuckoo_clock(time):
    (h, m) = list(map(int, time.split(':')))
    if m % 30 < 1:
        return ' '.join(['Cuckoo'] * (m == 30 or (h - 1) % 12 + 1))
    else:
        return ('Fizz ' * (m % 3 < 1) + 'Buzz ' * (m % 5 < 1))[:-1] or 'tick'
