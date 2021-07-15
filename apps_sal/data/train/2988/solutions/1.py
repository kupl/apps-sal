def reverse_and_combine_text(s):
    while ' ' in s:
        res = s.split(' ')
        s = ''
        while res:
            s += res.pop(0)[::-1]
            s += res.pop(0)[::-1] if res else ''
            s += ' ' if res else ''
    return s
