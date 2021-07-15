def define_suit(card):
    d={'C':'clubs','S':'spades','D':'diamonds','H':'hearts'}
    return d.get(card[-1])
