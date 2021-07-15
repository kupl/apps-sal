def remove_duplicate_words(s):
    lst = s.split()
    lst_new = []
    for i in lst:
        if i not in lst_new:
            lst_new.append(i)
    
    
    return ' '.join(lst_new)
