def how_many_dalmatians(number):
    if 1 <= number <= 10:
        return 'Hardly any'
    elif 11 <= number <= 50:
        return 'More than a handful!'
    elif 51 <= number <= 100:
        return "Woah that's a lot of dogs!"
    elif number == 101:
        return '101 DALMATIONS!!!'
