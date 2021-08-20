L = ('Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!')


def how_many_dalmatians(n):
    return L[(n > 10) + (n > 50) + (n == 101)]
