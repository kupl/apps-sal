def Split(a):
    no = []
    for i, x in a:
        if no and (i == x) == (no[-1][0] == no[-1][1]):
            yield no
            no = []
        no.append((i, x))
    yield no


for sq in Split((i + 1, int(input())) for i in range(int(input()))):
    tb = [0, 0]
    for np, goal in sq:
        if goal != np:
            if goal < tb[np < goal] or goal > sq[-1][0] or goal < sq[0][0]:
                print("No")
                return
            tb[np < goal] = goal
print("Yes")
