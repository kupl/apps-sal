def how_many_dalmatians(number):
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    return dogs[(number > 10) + (number > 50) + (number == 101)]
