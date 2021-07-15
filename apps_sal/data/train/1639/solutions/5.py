import itertools

def gta(limit, *args): # find the base_list first

    x = max(len(str(l)) for l in args)

    y = ''
    for i in range(x):
        for ix in args:
            try:
              if str(ix)[i] in y:
                  continue
              y += str(ix)[i]
            except:
                pass
    ans = 0   
    for i in range(1, limit+1):
        for xc in itertools.permutations(y[:limit], i):
            ans += sum([sum(map(int, xc))])
    
    return ans
