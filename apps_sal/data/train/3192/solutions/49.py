def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if 10 >= n:
        return dogs[0]
    elif 50 >= n > 10:
        return dogs[1]
    elif 100 >= n > 50:
        return dogs[2]
    elif n > 100:
        return dogs[3]
