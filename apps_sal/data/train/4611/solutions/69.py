def animals(h, l):
    # h = cw+ck => ck = h-cw
    # 4cw+2ck = l => 4cw + 2 h - 2cw = l => 2cw = l-2h => cw = l/2 - h => ck = 2h - l/2
    ck, cw = 2 * h - l // 2, l // 2 - h
    return (ck, cw) if ((h >= 0) and (l >= 0) and (not (l % 2)) and ck >= 0 and cw >= 0) else "No solutions"
