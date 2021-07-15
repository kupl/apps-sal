def promenade(choices):
    lm=[1,0]
    rs=[0,1]
    ans=[1,1]
    
    for i in choices:
        if i=='L':
            lm=ans[::]
            
        if i=='R':
            rs=ans[::]
        ans=[lm[0]+rs[0],lm[1]+rs[1]]
    return tuple(ans)
    
def fraction_to_promenade(fraction):
    ans=""
    frac=list(fraction)
    while(frac[0]!=frac[1]):
        if frac[0]>frac[1]:
        
            ans+="R"
            frac[0]=frac[0]-frac[1]
        if frac[1]>frac[0]:
            ans+="L"
            frac[1]=frac[1]-frac[0]
    return ans
