from itertools import cycle
def zozonacci(pattern, length):
    if not pattern or not length:return []
    
    fib=lambda lst:sum(lst[-2:])
    jac=lambda lst:lst[-1]+2*lst[-2]
    pad=lambda lst:lst[-2]+lst[-3]
    pel=lambda lst:2*lst[-1]+lst[-2]
    tet=lambda lst:sum(lst[-4:])
    tri=lambda lst:sum(lst[-3:])
    
    FIRST={"fib":[0,0,0,1],"jac":[0,0,0,1],"pad":[0,1,0,0],"pel":[0,0,0,1],"tri":[0,0,0,1],"tet":[0,0,0,1]}
    NEXT={"fib":fib,"jac":jac,"pad":pad,"pel":pel,"tet":tet,"tri":tri}
    
    seq=FIRST[pattern[0]]
    pattern=cycle(pattern)
    
    for i in range(length-4):
        seq.append(NEXT[next(pattern)](seq))
    
    return seq[:length]
