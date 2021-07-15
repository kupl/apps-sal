def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def gcd_matrix(a,b):
    g=[]
    for i in a:
        for j in b:
            g.append(gcd(i,j))
    
    return round(sum(g)/len(g),3)
