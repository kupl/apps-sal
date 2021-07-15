geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

import re

def goose_filter(birds):
    listn = []
    for i in birds:
        if i not in geese:
            listn.append(i)
    return listn
