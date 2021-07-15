from datetime import datetime as dt

def half_life(p1, p2):
    d1, d2 = (dt.strptime(p, "%Y-%m-%d") for p in sorted((p1, p2)))
    return (d2 + (d2 - d1)).strftime("%Y-%m-%d")
