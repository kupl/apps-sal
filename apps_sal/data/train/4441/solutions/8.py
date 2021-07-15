def chmod_calculator(perm):
    val = {"r": 4, "w": 2, "x": 1, "-": 0}
    scope = ("user", "group", "other")
    return "".join(str(sum(val[c] for c in perm.get(s, "---"))) for s in scope)
