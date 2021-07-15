def guess_my_number(guess, number = '123-451-2345'):
    digits = set('0123456789') - set(guess)
    for d in digits:
        number = number.replace(d, '#')
    return number
