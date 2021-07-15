def remove_duplicate_words(s):
    
    D = []
    words = s.split(" ")
    
    for word in words:
        
        if word not in D:
            D.append(word)
        else:
            pass
        
    return " ".join(D)

