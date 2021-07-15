def shortest_to_char(s,c):
    i = s.find(c)
    if i==-1 or not c: return []
    
    lst = list(reversed(range(1,i+1)))
    while i != -1:
        j = s.find(c,i+1)
        if j == -1:
            lst.extend(range(len(s)-i))
        else:
            x = j-i>>1
            lst.extend(range(0,x+1))
            lst.extend(reversed(range(1,j-i-x)))
        i = j
    return lst
