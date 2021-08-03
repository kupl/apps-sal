from itertools import cycle, dropwhile, islice


def whoseMove(lastPlayer, win):
    order = dropwhile(lastPlayer.__eq__, cycle(('black', 'white')))
    return win and lastPlayer or next(order)
