def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))
