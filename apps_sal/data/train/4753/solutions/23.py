geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    result = []
    for i in birds:
            if i != geese[0] and i != geese[1] and i != geese[2] and i != geese[3] and i != geese[4]:
                result.append(i)
    return result

