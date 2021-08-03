def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if number <= 10:
        return dogs[0]
    elif 10 < number <= 50:
        return dogs[1]
    elif number == 101:
        return dogs[3]
    elif 50 < number < 101:
        return dogs[2]
