def is_uppercase(inp):
    tv = True
    for x in range(0, len(inp)):
        if inp[x] > 'a' and inp[x] < 'z':
            tv = False
    return tv
