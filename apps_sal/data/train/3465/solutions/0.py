def valid_card(card):
    s = list(map(int, str(card.replace(' ', ''))))
    s[0::2] = [d * 2 - 9 if d * 2 > 9 else d * 2 for d in s[0::2]]
    return sum(s) % 10 == 0
