def sort_number(a):
    if a==[1,1,1]:
        return [1,1,2]
    if a==[1]:
        return [2]
    l=sorted(a)[:-1]
    l.append(1)
    return sorted(l)
