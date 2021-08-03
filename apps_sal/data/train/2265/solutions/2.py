def Split(a):
    no = []
    for i, x in a:
        if no:
            is_ok = i == x
            la_ok = no[-1][0] == no[-1][1]
            if is_ok == la_ok:
                yield no
                no = []
        no.append((i, x))
    yield no


n = int(input())
p = list(enumerate((int(input()) for i in range(n)), 1))
for sq in Split(p):
    tl = tr = 0
    for np, goal in sq:
        if goal > np:
            if goal < tr or goal > sq[-1][0]:
                print("No")
                return
            tr = goal
        elif goal < np:
            if goal < tl or goal < sq[0][0]:
                print("No")
                return
            tl = goal
print("Yes")
