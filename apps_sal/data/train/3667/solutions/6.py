def mid_endian(n):
    x = hex(n)[2:]
    x = '0' + x if len(x) % 2 != 0 else x
    lst = [x.upper()[i:i + 2] for i in range(0, len(x), 2)]
    ans = []
    for (i, e) in enumerate(lst):
        if i % 2 == 0:
            ans.append(e)
        else:
            ans.insert(0, e)
    return ''.join(ans)
