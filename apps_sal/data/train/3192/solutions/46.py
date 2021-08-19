def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if number == 101:
        return dogs[3]
    elif number > 50:
        return dogs[2]
    elif number > 11:
        return dogs[1]
    else:
        return dogs[0]

# respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
