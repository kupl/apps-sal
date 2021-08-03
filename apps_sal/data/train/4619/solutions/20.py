from itertools import cycle, dropwhile, islice


def whoseMove(last, win): return next(islice(dropwhile(last.__eq__, cycle(('black', 'white'))), win, win + 1))
