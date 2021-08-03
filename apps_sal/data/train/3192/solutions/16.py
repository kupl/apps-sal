def how_many_dalmatians(n):

    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

    if n == 101:
        return dogs[3]

    elif n > 50:
        return dogs[2]

    elif n <= 10:
        return dogs[0]

    else:
        return dogs[1]
