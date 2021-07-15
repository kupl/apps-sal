def pattern(n):
    t = []
    for i in range(1,n+1):
        t.append( (n-i)*" " + ls(i)+ +(n-i)*" ")
    return "\n".join(t)
    
def ls(k):
    ls = [str(j%10) for j in range(1,k)]
    return "".join(ls) + str(k%10) + "".join(ls[::-1])
