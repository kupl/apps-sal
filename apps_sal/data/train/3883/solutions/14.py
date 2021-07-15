from itertools import chain, zip_longest

def solve(s):
    ls_vow = sorted([x for x in s if x in "aeiou"])
    ls_con = sorted([x for x in s if x not in "aeiou"])
    if abs(len(ls_vow) - len(ls_con)) > 1 : return "failed"
    arr = [ls_vow, ls_con] if len(ls_vow)>=len(ls_con) else [ls_con, ls_vow]
    return "".join(list(chain(*list(zip_longest(*arr, fillvalue=''))))) 
