from random import choice


def random_case(x):
    final = ''
    for i in x:
        do = choice(('l', 'u'))
        final += (i.lower() if do == 'l' else i.upper())
    return final
