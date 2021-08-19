def encode(s):
    (s, sub_s) = (s.split(' '), '')
    for char in s:
        sub_s += char[::-1][1:] + char[-1] + ' '
    return sub_s[:-1]
