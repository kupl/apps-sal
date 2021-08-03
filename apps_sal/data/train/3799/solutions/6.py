from itertools import cycle, islice
from collections import Counter


def baubles_on_tree(baubles, branches):
    return [Counter(islice(cycle(range(branches)), baubles))[x] for x in range(branches)] or "Grandma, we will have to buy a Christmas tree first!"
