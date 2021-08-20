def how_many_dalmatians(number: int) -> str:
    dogs = ['Hardly any', 'More than a handful!', "Woah that's a lot of dogs!", '101 DALMATIONS!!!']
    respond = dogs[0] if number <= 10 else dogs[1] if number <= 50 else dogs[2] if number >= 50 and number <= 100 else dogs[3]
    return respond
