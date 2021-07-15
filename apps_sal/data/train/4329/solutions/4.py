def pig_latin(s):
    if not s.isalpha(): return None
    s  = s.lower()
    iV = next((i for i,c in enumerate(s) if c in "aeiou"), len(s))
    return s[iV:] + (s[:iV] or 'w') + "ay"
