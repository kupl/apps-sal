def greatest_product(n):
    l=len(n)
    t=[]
    for i in range(l-4):
        a=int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])
        t.append(a)
    print(t)
    ans=max(t)
    return(ans)
