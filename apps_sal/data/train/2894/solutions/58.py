def triple_trouble(one, two, three):
    list = map(lambda a,b,c: a+b+c, one,two, three)
    return "".join(list)
