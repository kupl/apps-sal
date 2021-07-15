how_to_find_them=lambda rt:{d:rt[d]if d in rt else(rt["a"]**2+rt["b"]**2)**.5if d=="c"else(rt["c"]**2-rt[(set("ab")^{d}).pop()]**2)**.5for d in"abc"}
