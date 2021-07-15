geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
from itertools import filterfalse
def goose_filter(birds):
    return list(filterfalse(lambda x: x in geese, birds))
