from enum import Enum
from collections import Counter
from itertools import chain
from operator import itemgetter, attrgetter


def roman_fractions(integer, fraction=0):
    if not (0 <= integer <= 5000 and 0 <= fraction < 12):
        return 'NaR'
    if integer == 0 and fraction == 0:
        return 'N'

    class Rom (Enum):
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

    def paired_romans():
        negatives = Counter({Rom.I: 2, Rom.X: 2, Rom.C: 2})
        for digit, prefix in zip(Rom, chain([None], negatives.elements())):
            yield (digit,), digit.value
            if prefix:
                yield (prefix, digit), digit.value - prefix.value

    def greedy_collect(iter_symbols, total):
        symbols = []
        symbol, value = next(iter_symbols)
        while total:
            if total >= value:
                total -= value
                symbols.extend(symbol)
            else:
                symbol, value = next(iter_symbols)
        return symbols

    extended_romans = iter(sorted(paired_romans(), key=itemgetter(1), reverse=True))
    symbols = greedy_collect(extended_romans, integer)
    integer_part = ''.join(symbol.name for symbol in symbols)

    fractions = iter(list({'S': 6, ':.:': 5, ':': 2, '.': 1}.items()))
    symbols = greedy_collect(fractions, fraction)
    fractional_part = ''.join(symbols)

    return integer_part + fractional_part
