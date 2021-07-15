def triangle(row):
    d = {'R':0,'G':1,'B':2}
    a = [d.get(_) for _ in row]
    while len(a)>1:
        a = list(map(lambda _:-(_[0]+_[1]),zip(a,a[1:])))
    return list(d.keys())[a[0]%3]
