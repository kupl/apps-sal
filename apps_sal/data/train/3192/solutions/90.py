def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        respond = dogs[0]
        return respond
    elif n <= 50:
        respond = dogs[1]
        return respond
    if n < 101:
        respond = dogs[2]
        return respond
    elif n == 101:
        respond = dogs[3]
        return respond
