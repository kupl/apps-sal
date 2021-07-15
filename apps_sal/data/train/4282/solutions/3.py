def hungry_seven(n):
    r=''.join([str(x) for x in n])
    while '789' in r:
        for x in range(len(r)):
            if r[x:x+3]=='789':
                r=r[:x]+r[x+1:]
                r=r[:x+2]+'7'+r[x+2:]
    g= [int(x) for x in r]
    return g
