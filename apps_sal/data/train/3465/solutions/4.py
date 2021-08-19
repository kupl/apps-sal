def valid_card(card):
    card = str(card.replace(' ', ''))
    return (sum(map(int, str(card)[1::2])) + sum((sum(map(int, str(i * 2))) for i in map(int, str(card)[0::2])))) % 10 == 0
