geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    geese_set = set(geese)
    return [elem for elem in birds if elem not in geese_set]
            

