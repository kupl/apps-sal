t = int(input())
ans = []
while t:
    X = []
    Y = []
    XY = []
    t -= 1
    n = int(input())
    st = ''
    for i in range(1, n + 1):
        (xi, yi) = list(map(int, input().split()))
        X.append(xi)
        Y.append(yi)
        XY.append((xi, yi))
    lborder = X.index(min(X))
    rborder = X.index(max(X))
    tborder = Y.index(max(Y))
    bborder = Y.index(min(Y))
    if (X[lborder], Y[tborder]) in XY:
        st = '1\n' + str(XY.index((X[lborder], Y[tborder])) + 1) + ' SE'
    elif (X[lborder], Y[bborder]) in XY:
        st = '1\n' + str(XY.index((X[lborder], Y[bborder])) + 1) + ' NE'
    elif (X[rborder], Y[tborder]) in XY:
        st = '1\n' + str(XY.index((X[rborder], Y[tborder])) + 1) + ' SW'
    elif (X[rborder], Y[bborder]) in XY:
        st = '1\n' + str(XY.index((X[rborder], Y[bborder])) + 1) + ' NW'
    elif rborder == lborder:
        st = '1\n' + str(tborder + 1) + ' SE'
    elif tborder == bborder:
        st = '1\n' + str(lborder + 1) + ' NE'
    elif Y[lborder] >= Y[rborder]:
        st = '2\n' + str(lborder + 1) + ' SE\n' + str(rborder + 1) + ' NW'
    else:
        st = '2\n' + str(lborder + 1) + ' NE\n' + str(rborder + 1) + ' SW'
    ans.append(st)
for x in ans:
    print(x)
