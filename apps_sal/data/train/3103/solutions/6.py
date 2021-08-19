def unique(integers):
    seen = set()
    return [x for x in integers if not (x in seen or seen.add(x))]
