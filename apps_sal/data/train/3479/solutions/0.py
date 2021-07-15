def p(t,k,n,l=1):
    if t<l: pass
    elif k==1 and t!=n: yield [t]
    else: yield from ([m]+s for m in range(l,t-l+1) for s in p(t-m,k-1,n,m) if m!=n)

def part_const(t,k,n): return sum(1 for _ in p(t,k,n))
