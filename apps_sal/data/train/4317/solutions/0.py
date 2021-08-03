vals = '2345678910JQKA'


def card_game(card_1, card_2, trump):
    print((card_1, card_2, trump))
    if card_1 == card_2:
        return 'Someone cheats.'
    elif 'joker' in [card_1, card_2]:
        return ['The first card won.', 'The second card won.'][card_1 != 'joker']
    elif card_1[-1] == card_2[-1]:
        return ['The first card won.', 'The second card won.'][vals.index(card_2[0]) > vals.index(card_1[0])]
    elif card_1[-1] != trump != card_2[-1]:
        return 'Let us play again.'
    else:
        return ['The first card won.', 'The second card won.'][card_1[-1] != trump]
