DOGS = [
    "Hardly any",
    "More than a handful!",
    "Woah that's a lot of dogs!",
    "101 DALMATIONS!!!",
]


def how_many_dalmatians(number):
    if number <= 10:
        respond = DOGS[0]
    elif number <= 50:
        respond = DOGS[1]
    elif number == 101:
        respond = DOGS[3]
    else:
        respond = DOGS[2]
    return respond
