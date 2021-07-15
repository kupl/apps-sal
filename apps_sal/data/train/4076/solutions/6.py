V,C = 'vowels consonants'.split()

def get_count(s=None):
    d={V:0,C:0}
    if not isinstance(s,str): return d
    for c in s.lower():
        if c in 'aeiou':  d[V]+=1
        elif c.isalpha(): d[C]+=1
    return d
