from math import pi
digs='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def converter(n, decimals=0, base=pi):
    neg=''
    ans=''
    if n<0:
        neg='-'
        n=-n
    for i in range(20,-20,-1):
        if i==-1-decimals: break
        if i==-1: ans+='.'
        d=int(n /(base**i))
        ans+=digs[d]
        n-=d*base**i
    while len(ans)>1 and ans[0]=='0' and ans[1]!='.': ans=ans[1:]
    return neg+ans
