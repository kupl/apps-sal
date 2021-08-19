def cards_and_pero(s):
    cards = [(s[i], s[i + 1:i + 3]) for i in range(0, len(s), 3)]
    if len(set(cards)) != len(cards):
        return [-1] * 4
    result = [13] * 4
    for (suit, num) in cards:
        result['PKHT'.index(suit)] -= 1
    return result
