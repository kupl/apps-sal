def define_suit(card):
    d = {'S':'spades','D':'diamonds','H':'hearts','C':'clubs'}
    return d[card[1]] if len(card)<3 else d[card[2]]
