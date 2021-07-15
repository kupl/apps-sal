
def get_char_count(s):
    print(s)
    ls = []
    ls2 = []
    d ={}
    nd = {}
    s = s.lower()
    for i in s:
        if i.isalpha() or i.isnumeric():
            ls.append(i)
    st = set(ls)
    for i in st: 
        ls2.append((s.count(i), i))
        
   
    for i in st:
        d[s.count(i)] = []
    x = 0
    for i in ls2:
        d[ls2[x][0]].append(ls2[x][1])
        x += 1
    
    for i in sorted(d,reverse = True):
        nd[i] = sorted(d[i])
        
    return(nd)

        
    

