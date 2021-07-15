def score_hand(cards):
    s = sum( c=='A' or c.isdigit() and int(c) or 10 for c in cards)
    n = cards.count('A')
    return s + 10 * (n and s<12)
