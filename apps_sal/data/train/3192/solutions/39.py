def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    respond = {n<=10: dogs[0], n<= 50 and n > 10: dogs[1], n==101: dogs[3]}.get(True, dogs[2])

    return respond
