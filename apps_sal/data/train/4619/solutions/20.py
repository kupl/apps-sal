from itertools import cycle, dropwhile, islice

whoseMove = lambda last, win: next(islice(dropwhile(last.__eq__, cycle(('black', 'white'))), win, win + 1))

