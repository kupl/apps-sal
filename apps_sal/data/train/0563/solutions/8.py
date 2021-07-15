def c(data):
    n,a,q,q_i=data
    res=[]
    for s,e in q_i:
        res.append(str(sum(a[s-1:e])))
    return '\n'.join(res)

def l():
    r=[]
    for _ in range(int(input())):
        n=int(input())
        a=[int(x)for x in input().split()]
        q=int(input())
        q_i=[tuple([int(x) for x in input().split()])for _ in range(q)]
        r.append((n,a,q,q_i))
    return r
def __starting_point():
    print('\n'.join(map(c,l())))
__starting_point()
