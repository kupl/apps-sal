geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

import itertools
def goose_filter(birds):
    a=[n for n in birds if n not in geese]
    return a
