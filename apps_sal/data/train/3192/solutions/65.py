def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n <= 10:
        return dogs[0]
    if 10 < n <= 50:
        return dogs[1]
    if 50 < n <= 100:
        return dogs[2]
    else:
        return dogs[3]
