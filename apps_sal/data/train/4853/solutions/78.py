def double_char(s):
    s = [lett * 2 for lett in s]
    y = ''
    x = 0
    while x < len(s):
        y += s[x]
        x += 1
    return y
