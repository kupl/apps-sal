def how_many_dalmatians(number):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    return dogs[0] if number <= 10 else dogs[1] if 10 < number <= 50 else dogs[3] if number == 101 else dogs[2]
