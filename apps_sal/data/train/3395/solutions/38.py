def remove_duplicate_words(s):
    
    l = []
    
    for i in s.split():
        if not i in l:
            l.append(i)
        else:
            pass
    return ' '.join(l)
