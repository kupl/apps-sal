def highest_age(g1, g2):
    d = {}
    for p in g1 + g2:
        name, age = p["name"], p["age"]
        d[name] = d.setdefault(name, 0) + age
    return max(sorted(d.keys()), key=d.__getitem__)

