def yes_no(a):
    if len(a) <= 1:
        return a
    a.append(a.pop(1))
    return [a.pop(0)] + yes_no(a)
