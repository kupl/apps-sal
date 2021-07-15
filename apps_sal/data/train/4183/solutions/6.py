greatest_distance=lambda a:max(len(a)-a[::-1].index(e)-a.index(e)-1for e in a)
