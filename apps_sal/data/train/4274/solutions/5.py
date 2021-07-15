import re
import operator as op
import functools as fn
import itertools as it

def do_math (string):
    def parse_item (string):
        letter_pattern = r'\D'
        letter = re.search(letter_pattern, string).group(0)
        number = int(re.sub(letter_pattern, '', string))
        return letter, number

    items = sorted(map(parse_item, string.split()), key=op.itemgetter(0))

    operations = it.chain([op.add], it.cycle([op.add, op.sub, op.mul, op.truediv]))
    def reducer (accum, operation):
        (_, value), operator = operation
        return operator(accum, value)
    result = fn.reduce(reducer, zip(items, operations), 0)
    return round(result)
