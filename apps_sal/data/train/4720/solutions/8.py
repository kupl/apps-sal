def hyperrectangularity_properties(r):
    z = [len(r)]
    while len(r):
        if len(set(type(v) for v in r)) == 1:
            if type(r[0]) == list:
                if len(set(len(rr) for rr in r)) != 1:
                    return None
                z.append(len(r[0]))
                r = [v for rr in r for v in rr]
            else:
                break
        else:
            return None
    return tuple(z)
