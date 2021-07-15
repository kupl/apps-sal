def group_groceries(s):
    d = {x: [] for x in "fruit meat other vegetable".split()}
    for x in s.split(","):
        a, b = x.split("_")
        d[a if a in d else "other"].append(b)
    return "\n".join(f"{x}:{','.join(sorted(y))}" for x, y in d.items())
