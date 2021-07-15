def define_suit(card):
    dicc={
        'C':'clubs', 
        'D':'diamonds', 
        'H':'hearts', 
        'S':'spades'
    }
    return dicc[card[-1:].upper()]
