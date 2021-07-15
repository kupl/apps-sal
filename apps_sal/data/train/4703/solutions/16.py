def bar_triang(pa, pb, pc, n=3., r=round):
    return [r((pa[0]+pb[0]+pc[0])/n,4), r((pa[1]+pb[1]+pc[1])/n,4)]
