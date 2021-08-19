dict_units = {0: 'Woda', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'piec', 6: 'szesc', 7: 'siedem', 8: 'osiem', 9: 'dziewiec'}
dict_units_1 = {10: 'dziesiec', 11: 'jedenascie', 12: 'dwanascie', 13: 'trzynascie', 14: 'czternascie', 15: 'pietnascie', 16: 'szesnascie', 17: 'siedemnascie', 18: 'osiemnascie', 19: 'dziewietnascie'}
dict_dec = {10: 'dziesiec', 20: 'dwadziescia', 30: 'trzydziesci', 40: 'czterdziesci', 50: 'piecdziesiat', 60: 'szescdziesiat', 70: 'siedemdziesiat', 80: 'osiemdziesiat', 90: 'dziewiecdziesiat'}


def ordering_beers(beers):
    if beers > 99:
        raise Exception
    length = len(str(beers))
    digit_l = None
    digit_r = None
    beer_word = None
    please = 'poprosze'
    if length > 1:
        if beers in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            return '{} {} {}'.format(dict_dec[beers].capitalize(), 'piw', please)
        elif beers in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
            return '{} {} {}'.format(dict_units_1[beers].capitalize(), 'piw', please)
        digit_l = int(str(beers)[0])
        digit_r = int(str(beers)[1])
        if digit_r in [2, 3, 4]:
            beer_word = 'piwa'
        elif digit_r == 1:
            beer_word = 'piw'
        elif digit_r == 0:
            beer_word = 'mineralna'
        else:
            beer_word = 'piw'
        return '{} {} {} {}'.format(dict_dec[digit_l * 10].capitalize(), dict_units[digit_r], beer_word, please)
    else:
        digit_r = int(beers)
        if digit_r in [2, 3, 4]:
            beer_word = 'piwa'
        elif digit_r == 1:
            beer_word = 'piwo'
        elif digit_r == 0:
            beer_word = 'mineralna'
        else:
            beer_word = 'piw'
        if beers == 1:
            return '{} {} {}'.format('Jedno'.capitalize(), beer_word, please)
        return '{} {} {}'.format(dict_units[digit_r].capitalize(), beer_word, please)
