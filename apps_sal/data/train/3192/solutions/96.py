def how_many_dalmatians(n):
    if n == 101:
        return '101 DALMATIONS!!!'
    elif n in range(11):
        return 'Hardly any'
    elif n in range(11, 51):
        return 'More than a handful!'
    else:
        return 'Woah that\'s a lot of dogs!'
