import re
def vowel_shift(s,n):
    vow = re.sub(r'[^aeiouAEIOU]',"",s or "")
    if not s or n == 0 or not vow: return s
    n %= len(vow)
    vow = iter(vow[-n:] + vow[:-n])
    return "".join(i if i not in "aeiouAEIOU" else next(vow) for i in s)
