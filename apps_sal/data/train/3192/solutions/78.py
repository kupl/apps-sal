def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    result = ''
    if n <= 10:
        result = dogs[0]
    elif n <= 50:
        result = dogs[1]
    elif n == 101:
        result = dogs[3]
    else:
        result = dogs[2]
    return result
