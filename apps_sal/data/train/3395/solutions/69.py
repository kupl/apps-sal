def remove_duplicate_words(s):
    
    z = []
    s = s.split()
    
    for i in s:
        if i not in z:
            z.append(i)
            
    return " ".join(z)
