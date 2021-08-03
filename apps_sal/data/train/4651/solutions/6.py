def christmas_tree(height):
    h = height - height % 3
    n, r = h // 3, ''
    sz, l1, l2, l3, k = 5 + (n - 1) * 2, '*', '***', '*****', '\r\n'
    w = (sz - len(l1)) // 2
    for i in range(n):
        r += ' ' * w + l1 + k
        r += ' ' * (w - 1) + l2 + k
        r += ' ' * (w - 2) + l3 + k
        w -= 1
        l1 += '**'
        l2 += '**'
        l3 += '**'
    return r + ' ' * ((sz - 3) // 2) + '###' if height > 2 else ''
