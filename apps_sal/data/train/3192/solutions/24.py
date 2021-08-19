def how_many_dalmatians(n):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    if n == 101:
        return dogs[3]
    elif n == None:
        return dogs[2]
    elif 51 < n < n ** n:
        return dogs[2]
    elif 10 < n <= 50:
        return dogs[1]
    elif n <= 10:
        return dogs[0]
