def guess_my_number(guess, number='123-451-2345'):
    g = set(guess + '-')
    return ''.join((x if x in g else '#' for x in number))
