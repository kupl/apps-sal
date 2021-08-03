def reverseWords(s):
    s = s.split(' ')
    r = ''
    for x in range(0, len(s)):
        r += s[len(s) - x - 1]
        if x != len(s) - 1:
            r += ' '
    return r
