import re

def sursurungal(stg):
    return re.sub(r"(\d+) (\w+)", sur_grp, stg)

def sur_grp(m):
    n, w = (int(c) if c.isdigit() else c for c in m.groups())
    p, s = ("", w[-1]) if n < 2 else ("bu", "") if n == 2 else ("", "zo") if n < 10 else ("ga", "ga")
    return f"{n} {p}{w[:-1]}{s}"
