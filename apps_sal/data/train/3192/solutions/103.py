def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

    # respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]

    if number <= 10:
        respond = dogs[0]
    elif number <= 50:
        respond = dogs[1]
    elif number == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]

    return respond
