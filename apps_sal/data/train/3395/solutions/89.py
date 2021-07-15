def remove_duplicate_words(s):
    res = []
    s = s.split(' ')
    
    for w in s:
        if w not in res:
            res.append(w)
            
    erg = ""
    for r in res:
        erg += r + " "
        
    return erg[:-1]
