def wanted_words(n, m, forbid_let):
    import re
    vov = "[aeiou]"
    cons = "[qwrtpysdfghjklzxcvbnm]"
    fb = "[" + ''.join(forbid_let) + "]"
    return [word for word in WORD_LIST if len(re.findall(vov, word)) == n and len(re.findall(cons, word)) == m and len(re.findall(fb, word)) == 0]
