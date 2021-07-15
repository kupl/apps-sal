from collections import Iterable
from itertools import chain

def flatten_me(lst):
    return list(chain(*(x if isinstance(x,Iterable) else [x] for x in lst)))

