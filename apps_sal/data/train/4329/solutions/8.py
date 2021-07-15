def pig_latin(s):
    if not s.isalpha(): return None
    s =s.lower()
    if s[0] in 'aeiou': return s+'way'
    for n,i in enumerate(s):
        if i in 'aeiou':
            return s[n:]+s[0:n]+'ay'
    return s+'ay'
