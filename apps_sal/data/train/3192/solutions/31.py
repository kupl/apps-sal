def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

    if n <= 10:
        x = 0
    elif n <= 50:
        x = 1
    elif n == 101:
        x = 3
    else:
        x = 2

    return dogs[x]
