def tiy_fizz_buzz(x):
    return ''.join((('Iron' * e.isupper() + ' ' + 'Yard' * (e.lower() in 'aiueo')).strip() or e for e in x))
