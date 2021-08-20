def sort_poker(john, uncle):
    card_order = '23456789TJQKA'
    suit_order = [('S', uncle.index('S')), ('D', uncle.index('D')), ('H', uncle.index('H')), ('C', uncle.index('C'))]
    suit_order = [X[0] for X in sorted(suit_order, key=lambda x: x[1])]
    john = john.replace('10', 'T')
    john = [john[i:i + 2] for i in range(0, len(john), 2)]
    john = sorted(john, key=lambda x: (suit_order.index(x[0]), card_order.index(x[1])))
    return ''.join(john).replace('T', '10')
