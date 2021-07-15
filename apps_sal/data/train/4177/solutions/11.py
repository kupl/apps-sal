def men_from_boys(a):
    x = sorted(filter(lambda _: _%2,list(set(a))),reverse = True)
    y = sorted(filter(lambda _: not _%2,list(set(a))))
    return y+x
