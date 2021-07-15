def pig_latin(s):
    if s.isalpha():
        s = s.lower()
        if s[0] in 'aeiou':
            return s + 'way'
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s[0] in 'aeiou':
                break
        return s + 'ay'
        

