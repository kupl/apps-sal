def solve(a,b):
    unique=[]
    for i in a:
        if i not in b:
            unique.append(i)
    for i in b:
        if i not in a:
            unique.append(i)
            
    return "".join(unique)        
