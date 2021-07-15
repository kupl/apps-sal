def solve(s):
   
    l = []
    b = []
    for i, j in enumerate(list(s)):
        if j.isspace() == True:
            b.append(i)

            
        else:
            l.insert(0, (j))
            
    for k in b:
        l.insert(k, ' ')
    return ''.join(l)
