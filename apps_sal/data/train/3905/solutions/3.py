def missing(s):
    for k in range(1, 7):
        p, n, l, gaps = s, int(s[:k]), k, []
        while p:
            p = p[l:]
            if p.startswith(str(n+1)):
                l, n = len(str(n+1)), n + 1
            elif p.startswith(str(n+2)):
                gaps += [n + 1]
                l, n = len(str(n+2)), n + 2
            else: 
                break
        if len(gaps) == 1 and p == '': return gaps.pop()    
    return -1
