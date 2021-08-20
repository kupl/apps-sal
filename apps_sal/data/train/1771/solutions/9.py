def closure_gen(*seq):
    if not seq:
        return
    if seq == (1,):
        yield 1
        return
    if 1 in seq:
        yield 1
    seq = [i for i in seq if i != 1]
    (d, ind, li) = ({i: [i] for i in seq}, {i: 0 for i in seq}, [])
    while True:
        min_ = min((d[i][0] for i in d if d[i]))
        li.append(min_)
        yield min_
        for i in d:
            if d[i][0] == min_:
                d[i].pop(0)
            if not d[i]:
                d[i].append(li[ind[i]] * i)
                ind[i] += 1
