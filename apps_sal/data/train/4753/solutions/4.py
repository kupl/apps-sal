geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    
    for j in geese:    #For each element in geese
        for i in birds:    #For each element in birds 
            if i == j:
                birds.remove(i)                        
    return birds
