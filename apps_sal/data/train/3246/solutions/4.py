def majority(arr):
    #     d = {}
    #     l = []
    #     for elem in arr:
    #         d[elem] = arr.count(elem)
    #     for k,v in d.items():
    #         if v  == max(d.values()):
    #             l.append(k)
    #     return l[0] if len(l) == 1 else None

    d = {elem: arr.count(elem) for elem in arr}

    l = [k for k, v in list(d.items()) if v == max(d.values())]

    return l[0] if len(l) == 1 else None
