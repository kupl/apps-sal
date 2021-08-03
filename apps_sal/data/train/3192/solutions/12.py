DOGS = ((100, '101 DALMATIONS!!!'), (50, 'Woah that\'s a lot of dogs!'),
        (10, 'More than a handful!'), (0, 'Hardly any'))


def how_many_dalmatians(n):
    return next(msg for total_dogs, msg in DOGS if n > total_dogs)
