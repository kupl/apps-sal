def guess_my_number(guess, number='123-451-2345'):
    return ''.join(a if a in guess or a == '-' else '#' for a in number)

