def blocks(s):
    switch, ret = [ lambda e:e.islower(), lambda e:e.isupper(), lambda e:e.isdigit() ], ''
    for lm in switch:
        ret += ''.join([ e for e in sorted(s) if lm(e) ])       
    return ''.join( box(ret) )
    
def box(blok):
    if blok:
        ret = [ '' ] * blok.count( max(blok,key = blok.count) )
        for e in blok:
            for i in range(blok.count(e)):
                ret[i] += ['',e][e not in ret[i]]
        return '-'.join(ret)
    return blok

