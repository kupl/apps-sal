def hex_to_dec(s):
    s = s.lower()
    t = 0
    j = len(s) - 1
    A = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(len(s)):
        r = s[i]
        if type(s[i]) == str and 97 <= ord(s[i]) <= 102:
            r = ord(s[i]) - 87
        t += int(r) * 16 ** j
        j -= 1
    return t
