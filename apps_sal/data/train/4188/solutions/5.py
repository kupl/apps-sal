def find_dup(xs):
    found = set()
    for x in xs:
        if x in found:
            return x
        found.add(x)
