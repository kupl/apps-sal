def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

    if n <= 10:
        respond = 0
    elif n <= 50:
        respond = 1
    elif n == 101:
        respond = 3
    else:
        respond = 2

    return dogs[respond]
