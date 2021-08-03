def find_page_number(p):
    res = []
    x = 1
    for v in p:
        if v != x:
            res.append(v)
        else:
            x += 1
    return res
