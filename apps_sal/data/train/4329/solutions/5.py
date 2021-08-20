def pig_latin(s):
    (prev, s) = ('', s.lower())
    if any((ord(x) not in range(ord('a'), ord('z') + 1) for x in s)) or not s:
        return
    while s and s[0] not in 'aeiou':
        prev += s[0]
        s = s[1:]
    return f"{s}{prev}{('', 'w')[not prev]}ay"
