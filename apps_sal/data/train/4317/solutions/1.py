ORDERS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RESULTS = ['Let us play again.', 'The first card won.', 'The second card won.', 'Someone cheats.']


def f(c1, c2, trump):
    if c1 == c2:
        return -1
    if c1 == 'joker':
        return 1
    elif c2 == 'joker':
        return 2
    cards = (c1, c2)
    (n1, n2) = (ORDERS.index(c[:-1]) for c in cards)
    (s1, s2) = (c[-1] for c in cards)
    won = 0
    if s1 == s2:
        if n1 > n2:
            return 1
        elif n1 < n2:
            return 2
    elif s1 == trump:
        return 1
    elif s2 == trump:
        return 2
    return 0


def card_game(card_1, card_2, trump):
    return RESULTS[f(card_1, card_2, trump)]
