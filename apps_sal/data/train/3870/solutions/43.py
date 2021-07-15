def solve(s):
    spaceindex = []
    for i in range(0,len(s)):
        if s[i]==" ":
            spaceindex.append(i)
    
    s = s.replace(" ","")[::-1]
    
    sil = []
    for char in s:
        sil.append(char)
        
    for num in spaceindex:
        sil.insert(num," ")
    
    return "".join(sil)


