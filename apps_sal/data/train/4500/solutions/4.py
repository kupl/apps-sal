def define_suit(card):
    a = { 'C':'clubs', 'D':'diamonds', 'H':'hearts', 'S':'spades'}
    return a.get(card[-1])
