from itertools import zip_longest
def solve(s):
    vowels,consonants=[],[]
    for c in s:
        if c in 'aeiou':
            vowels.append(c)
        else:
            consonants.append(c)
    if abs(len(vowels)-len(consonants))>1:
        return 'failed'
    r=''
    a=[sorted(vowels),sorted(consonants)]
    if len(vowels)<len(consonants):
        a=a[::-1]
    for c1,c2 in zip_longest(*a,fillvalue=''):
        r+=c1+c2
    return r
