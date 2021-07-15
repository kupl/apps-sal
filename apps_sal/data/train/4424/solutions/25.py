def expression_matter(a, b, c):
    r = 0
    for o1 in ("+", "*"):
        for o2 in ("+", "*"):
            r = max(r, (max(eval("({} {} {}) {} {}".format(a, o1, b, o2, c)), eval("{} {} ({} {} {})".format(a, o1, b, o2, c)))))
    return r
