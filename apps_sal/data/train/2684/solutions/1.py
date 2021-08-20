def ordering_beers(beers):
    one_to_ten = {1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'piec', 6: 'szesc', 7: 'siedem', 8: 'osiem', 9: 'dziewiec'}
    ten_to_nineteen = {10: 'dziesiec', 11: 'jedenascie', 12: 'dwanascie', 13: 'trzynascie', 14: 'czternascie', 15: 'pietnascie', 16: 'szesnascie', 17: 'siedemnascie', 18: 'osiemnascie', 19: 'dziewietnascie'}
    twenty_to_ninety = {20: 'dwadziescia', 30: 'trzydziesci', 40: 'czterdziesci', 50: 'piecdziesiat', 60: 'szescdziesiat', 70: 'siedemdziesiat', 80: 'osiemdziesiat', 90: 'dziewiecdziesiat'}
    if 99 > beers < 0:
        raise Exception()
    if beers == 0:
        return 'Woda mineralna poprosze'
    else:
        beers_str = list(str(beers))
        piwa = [2, 3, 4]
        if len(beers_str) > 1:
            if 10 <= beers <= 19:
                return ten_to_nineteen[beers].capitalize() + ' piw poprosze'
            if beers >= 20:
                result = twenty_to_ninety[int(beers_str[0] + '0')].capitalize()
                return result + ' piw poprosze' if beers_str[1] == '0' else result + ' ' + one_to_ten[int(beers_str[1])] + ' piwa poprosze' if int(beers_str[1]) in piwa else result + ' ' + one_to_ten[int(beers_str[1])] + ' piw poprosze'
        else:
            ones = one_to_ten[int(beers_str[0])]
            return 'Jedno piwo poprosze' if beers == 1 else str(ones).capitalize() + ' piwa poprosze' if beers in piwa else str(ones).capitalize() + ' piw poprosze'
