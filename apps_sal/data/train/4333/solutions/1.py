def sort_number(a): 
    if max(a) != 1:
        a.remove(max(a))
        a.append(1)
    else:
        a.remove(max(a))
        a.append(2)
        
    return sorted(a)

