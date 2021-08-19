def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n > 100:
        respond = dogs[3]
    elif n > 50:
        respond = dogs[2]
    elif n > 10:
        respond = dogs[1]
    else:
        respond = dogs[0]
    return respond
