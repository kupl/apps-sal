def valid_card(card):
    return sum(([2 * c, 2 * c - 9][2 * c > 9] if i % 2 else c for (i, c) in enumerate(map(int, card.replace(' ', '')[::-1])))) % 10 == 0
