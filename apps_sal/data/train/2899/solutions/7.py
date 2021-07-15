def bin_str(s):
    c = 0
    x = '0'
    for i in s:
        if x != i:
                c += 1
                x = i
    return c
