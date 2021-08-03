VOWELS = set('aeiou')


def pig_latin(st):
    s = st.lower()
    if s.isalpha():
        if set(s) & VOWELS:
            if s[0] in VOWELS:
                s += 'w'
            while s[0] not in VOWELS:
                s = s[1:] + s[:1]
        return s + 'ay'
