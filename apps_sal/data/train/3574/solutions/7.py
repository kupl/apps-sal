def Dragon(n):
    if not isinstance(n, int) or n < 0:
        return ""
    d = "Fa"
    for i in range(n):
        d = "".join("aRbFR" if c == "a" else "LFaLb" if c == "b" else c for c in d)
    return d.translate(dict.fromkeys(map(ord, "ab")))
