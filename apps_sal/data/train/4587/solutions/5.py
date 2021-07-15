def range_parser(stg):
    result = []
    for rg in stg.split(","):
        rg, _, s = rg.partition(":")
        i, _, j = rg.partition("-")
        i, j, s = int(i), int(j or i) + 1, int(s or 1)
        result.extend(range(i, j, s))
    return result
