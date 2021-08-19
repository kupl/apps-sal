from collections import defaultdict


def cards_and_pero(s):
    deck = defaultdict(set)
    for n in range(0, len(s), 3):
        card = s[n:n + 3]
        if card[1:] in deck[card[0]]:
            return [-1, -1, -1, -1]
        deck[card[0]] |= {card[1:]}
    return [13 - len(deck[suit]) for suit in 'PKHT']
