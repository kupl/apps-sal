def ordering_beers(beers):
    num_0_to_19_in_polish = ('zero', 'jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec', 'dziesiec', 'jedenascie', 'dwanascie', 'trzynascie', 'czternascie', 'pietnascie', 'szesnascie', 'siedemnascie', 'osiemnascie', 'dziewietnascie')
    tens_10_to_90_in_polish = ('dziesiec', 'dwadziescia', 'trzydziesci', 'czterdziesci', 'piecdziesiat', 'szescdziesiat', 'siedemdziesiat', 'osiemdziesiat', 'dziewiecdziesiat')
    if beers == 0:
        number = 'Woda'
        beverage = 'mineralna'
    elif beers == 1:
        number = 'Jedno'
        beverage = 'piwo'
    elif beers <= 19 and beers > 0:
        number = num_0_to_19_in_polish[beers]
        if beers in (2, 3, 4):
            beverage = 'piwa'
        else:
            beverage = 'piw'
    elif beers <= 99 and beers > 0:
        tens = beers // 10
        remains = beers % 10
        if remains == 0:
            number = tens_10_to_90_in_polish[tens - 1]
        else:
            number = tens_10_to_90_in_polish[tens - 1] + ' ' + num_0_to_19_in_polish[remains]
        if remains in (2, 3, 4):
            beverage = 'piwa'
        else:
            beverage = 'piw'
    else:
        raise Exception('输入变量越界')
    number1 = number.capitalize()
    return number1 + ' ' + beverage + ' poprosze'
