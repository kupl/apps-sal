def pair_of_shoes(shoes):
    l = [i for i, j in shoes]
    m = [j for i, j in shoes]
    return sum(m.count(i) % 2 == 0 for i in set(m)) == len(set(m)) and l.count(0) == l.count(1)

