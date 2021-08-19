def div_con(l):
    return sum((e if type(e) == int else -int(e) for e in l))
