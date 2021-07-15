meeting = lambda s: "".join("({}, {})".format(ln, fn) 
    for ln, fn in sorted(p.split(":")[::-1] for p in s.upper().split(";")))
