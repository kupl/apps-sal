def shut_the_gate(farm):
    r=[]
    for g in farm.split('|'):
        if 'H' in g:
            g=g.replace('A','.').replace('V','.')
        elif 'R' in g:
            g=g.replace('V','.')
        r.append(g)
    if 'H' in r[-1]:
        r[0]=r[0].replace('A','.').replace('V','.')
    elif 'R' in r[-1]:
        r[0]=r[0].replace('V','.')
    if 'H' in r[0]:
        r[-1]=r[-1].replace('A','.').replace('V','.')
    elif 'R' in r[0]:
        r[-1]=r[-1].replace('V','.')
    r[0]=r[0].replace('H','.').replace('R','.').replace('C','.')
    r[-1]=r[-1].replace('H','.').replace('R','.').replace('C','.')
    return '|'.join(r)
