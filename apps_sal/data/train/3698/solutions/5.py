def translate(x):
    if x.isupper():
        if x not in 'AEIOU':
            return 'Iron'
        else:
            return 'Iron Yard'
    elif x not in 'aeiou' or not x.isalpha():
        return x
    else:
        return 'Yard'


def tiy_fizz_buzz(string):
    return ''.join((translate(c) for c in string))
