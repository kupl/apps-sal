def remove_duplicate_words(s):
    arr = s.split()
    new_arr = []
    for el in arr:
        if not el  in new_arr:
            new_arr.append(el)
    return  ' '.join(new_arr)
 
        

