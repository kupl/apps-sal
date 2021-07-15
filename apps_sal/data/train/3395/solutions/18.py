def remove_duplicate_words(s):
    tot = []
    for i in s.split():
        if i not in tot:
            tot.append(i)
    return ' '.join(tot)
    
    return ' '.join(tot)
