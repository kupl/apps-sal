from collections import Counter

def blocks(s):
    stg = sorted(sorted(set(s)), key = lambda x:(x.isdigit() ,x.isupper()))
    doc = Counter(s)
    ret = ''
    while max(doc.values(),default = 0)>0:
        for e in stg:
            if doc[e]>0:
                ret += e
            doc[e] -= 1   
        ret += '-'
    return ret[:-1]
