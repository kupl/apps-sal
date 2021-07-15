geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    salir = False
    while salir != True:
        salir = True
        for b in birds:
            if b in geese:
                birds.remove(b)
                salir = False
        
    return birds
