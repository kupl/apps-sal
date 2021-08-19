def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n <= 10:
        r = dogs[0]
    elif n > 10 and n <= 50:
        r = dogs[1]
    elif n == 101:
        r = dogs[3]
    else:
        r = dogs[2]
    return r
