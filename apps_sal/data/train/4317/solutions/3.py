def card_game(c1, c2, trump):
    if c1 == c2:
        return 'Someone cheats.'
    if 'joker' in [c1, c2]:
        return get_win(c2 == 'joker')
    if all((c1[-1] != c2[-1], any((c1[-1] == trump, c2[-1] == trump)))):
        return get_win(c2[-1] == trump)
    if c1[-1] == c2[-1]:
        (c1, c2) = ['234567891JQKA'.index(e) for e in [c1[0], c2[0]]]
        return get_win(c2 > c1)
    return 'Let us play again.'


def get_win(bool):
    return 'The {} card won.'.format(['first', 'second'][bool])
