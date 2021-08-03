def how_many_dalmatians(number):
    reaction = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return reaction[0] if number <= 10 else reaction[1] if number <= 50 else reaction[3] if number == 101 else reaction[2]
