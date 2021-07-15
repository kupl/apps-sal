from collections import Counter
def string_letter_count(s):
    c=Counter([c for c in s.lower() if c.isalpha()])
    r=''
    for k in sorted(c.keys()):
        r+=str(c[k])+k
    return r
