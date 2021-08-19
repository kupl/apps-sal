def animals(h, l):
    (ck, cw) = (2 * h - l // 2, l // 2 - h)
    return (ck, cw) if h >= 0 and l >= 0 and (not l % 2) and (ck >= 0) and (cw >= 0) else 'No solutions'
