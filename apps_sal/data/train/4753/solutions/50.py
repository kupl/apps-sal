geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    '''we will iterate through the array preserving order while excluding the aforemntioned geese list'''
    return [x for x in birds if x not in geese]
