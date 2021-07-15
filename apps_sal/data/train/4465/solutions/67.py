def super_size(n):
    
    list = []
    textNb = ""
    
    for nb in str(n):
        list.append(nb)
    
    list.sort(reverse=True)
    
    for ch in list:
        textNb += ch
        
    return int(textNb)
    

