def double_check(strng):
    return any((x.lower() == strng[i + 1].lower() for (i, x) in enumerate(strng[:-1])))
