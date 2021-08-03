import re


def sort_poker(john, uncle):
    SUITS = re.compile('[SHCD]')
    order = list(dict.fromkeys(SUITS.findall(uncle)))
    ord = {x: order.index(x) for x in order}
    john = re.findall('([CDHS])(\d+|[JKQA])', john)
    suit = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'K': 13, 'Q': 12, 'A': 14}
    a = [(ord[x[0]], suit[x[1]], str(x)) for x in john]
    a.sort(key=lambda x: x[1])
    a.sort(key=lambda x: x[0])
    return ''.join([x for x in ''.join([x[2] for x in a])if x.isalpha() or x.isnumeric()])
