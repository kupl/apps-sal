def save(sizes, hd): 
    if sum(sizes) <= hd:
        return len(sizes)
    for i in range(len(sizes)) :
        if sum(sizes[:i+1]) > hd:
            return i
    return 0
