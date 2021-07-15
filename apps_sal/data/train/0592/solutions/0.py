import sys

def mex(S,W,C,start,end):
    """Returns Nim-number of S[start:end]"""
    key=(start,end)
    try:
        return C[key]
    except KeyError:
        pass
    A=set()
    for s in range(start,end):
        for e in range(start+1,end+1):
            if S[s:e] not in W: continue
            A.add(mex(S,W,C,start,s)^mex(S,W,C,e,end))
    a=0
    while a in A: a+=1
    C[key]=a
    return a
    

a=sys.stdin
#a=open('astrgame.txt','r')
T=int(a.readline())
for t in range(T):
    S=a.readline().strip()
    N=int(a.readline())
    W=set([a.readline().strip() for n in range(N)])
    print('Teddy' if mex(S,W,{},0,len(S)) else 'Tracy')
    

