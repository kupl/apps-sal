def christmas_tree(height):
    if height < 3:
        return ''
    res = [1, 3, 5]
    for _ in range((height-3)//3):
        res.extend(res[-2:] + [res[-1]+2])
    w = max(res)
    ans = [('*' * r).center(w).rstrip() for r in res] + ['###'.center(w).rstrip()]
    return '\r\n'.join(ans)
