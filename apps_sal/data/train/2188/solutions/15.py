from sys import stdin
d,res,elem={},'','0101010101'
a=lambda:stdin.readline().split()
for _ in range(int(stdin.readline())):
    c,x=map(str,a())
    if c!='?':
        x=[*x]
        x=[elem[int(y)] for i,y in enumerate(x)]
        x=''.join(x)
    x=x[x.find('1'):]
    if c=='+':
        if d.get(x)==None:d[x]=0
        d[x]+=1
    elif c=='-':d[x]-=1
    else:
        if d.get(x)==None:res+='0'+'\n'
        else:res+=str(d[x])+'\n'
print(res)
