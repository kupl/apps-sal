def unused_digits(*l):
    digits_set = set(list("0123456789"))
    test_set = set("".join(str(i) for i in l))
    d = digits_set.difference(test_set)
    r = "".join(sorted(d))
    return r
