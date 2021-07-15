from itertools import zip_longest

def solve(s):
    vow = sorted(c for c in list(s) if c in 'aeiou')
    con = sorted(c for c in list(s) if c not in 'aeiou')
    if abs(len(vow)-len(con)) > 1: return 'failed'
    arr = [vow, con] if len(vow)>=len(con) else [con, vow]
    return ''.join(''.join(p) for p in list(zip_longest(*arr, fillvalue='')))
