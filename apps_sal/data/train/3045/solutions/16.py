def elevator(l, r, c): return ["right", "left"][abs(l - c) < abs(r - c)]
