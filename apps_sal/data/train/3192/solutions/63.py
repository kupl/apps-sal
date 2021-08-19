def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n < 11:
        return dogs[0]
    elif n > 11 and n < 52:
        return dogs[1]
    elif n > 50 and n < 101:
        return dogs[2]
    elif n == 101:
        return dogs[3]
