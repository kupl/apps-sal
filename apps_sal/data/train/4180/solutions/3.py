def lottery(stg):
    return "".join(c for c in sorted(set(stg), key=stg.index) if c.isdecimal()) or "One more run!"
