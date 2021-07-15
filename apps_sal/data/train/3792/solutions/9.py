from re import findall

def slogans(p, r):
    pattern = '(' + '|'.join(p[i:] for i in range(len(p))) + ')'
    return len(findall(pattern, r))
