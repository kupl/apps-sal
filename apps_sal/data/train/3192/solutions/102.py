def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

    if number == 101:
        return dogs[3]
    if number <= 10:
        return dogs[0]
    if number <= 50:
        return dogs[1]
    if number > 50:
        return dogs[2]
