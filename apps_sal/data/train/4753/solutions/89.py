geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    
    done = list()
    for word in birds:
        if word in geese:
            continue
        else:
            done.append(word)
    return done
