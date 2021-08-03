def is_alt(s):
    vowels = list("aeiou")
    v = s[0] in vowels

    for i in s:
        if (i in vowels) != v:
            return False
        v = not(v)
    return True
