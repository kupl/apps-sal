def save(sizes, hd): 
    return sum(1 for i in range(len(sizes)) if sum(sizes[:i+1])<=hd)
