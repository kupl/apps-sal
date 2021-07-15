geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def filtergeese(bird):
    if bird in geese:
        return False
    else:
        return True     

def goose_filter(birds): 
    return list(filter(filtergeese, birds))
  

