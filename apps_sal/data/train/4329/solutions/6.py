def pig_latin(s):
    a = ''
    if not s.isalpha(): return None
    s = s.lower()
    for i in s:
        if i in 'aeiou':
            break
        a+= i
    return s + 'way' if s[0] in 'aeiou' else s[len(a):] + a + 'ay'
