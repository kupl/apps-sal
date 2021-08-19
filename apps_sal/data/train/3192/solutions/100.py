def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n <= 10:
        r = dogs[0]
        return r
    elif n <= 50:
        r = dogs[1]
        return r
    elif n == 101:
        r = dogs[3]
        return r
    else:
        r = dogs[2]
        return r
