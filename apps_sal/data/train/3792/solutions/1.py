from re import findall

def slogans(p, r):
    return len(findall('|'.join(p[i:] for i in range(len(p))), r))
