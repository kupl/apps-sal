def card_game(card_1, card_2, t):
    if card_1 == card_2:
        return "Someone cheats."
    if card_1 == 'joker':
        return "The first card won."
    if card_2 == 'joker':
        return "The second card won."
    f_val = lambda v: int(v) if v.isdigit() else 10 + ' JQKA'.index(v)
    c1, t1 = f_val(card_1[:-1]), card_1[-1]
    c2, t2 = f_val(card_2[:-1]), card_2[-1]
    if t1 in [t, t2]:
        return f'The {["first", "second"][t2 == t1 and c2 > c1]} card won.'
    return "The second card won." if t2 == t else "Let us play again."
