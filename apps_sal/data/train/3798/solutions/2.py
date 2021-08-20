def cards_and_pero(s):
    cards = [s[i - 3:i] for i in range(3, len(s) + 1, 3)]
    if len(set(cards)) < len(cards):
        return [-1, -1, -1, -1]
    return [13 - len([card[0] for card in cards if card[0] == suit]) for suit in 'PKHT']
