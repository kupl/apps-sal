def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    response = ''
    if n == 101:
        response = dogs[3]
    elif n <= 10:
        response = dogs[0]
    elif n <= 50:
        response = dogs[1]
    else:
        return dogs[2]
    return response
