def remove_duplicate_words(s):
    split = s.split()
    newL = []
    for i in split:
        if i not in newL:
            newL.append(i)
            
    return ' '.join(newL)
