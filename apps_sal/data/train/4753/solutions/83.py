a = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(b):
    for x in a:
        for x in b:
            if x in a:
                b.remove(x)
    return b 
