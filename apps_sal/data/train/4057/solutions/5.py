def score_hand(cards):
    aces = [i for i in cards if i == 'A']
    cards = list(filter(lambda x: x is not 'A', cards))
    cards.extend(aces)
    total = 0
    for (i, card) in enumerate(cards):
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card is 'A':
            total += 11 if 11 <= 21 - total and ''.join(cards).rindex('A') == i else 1
        else:
            total += int(card)
    return total
