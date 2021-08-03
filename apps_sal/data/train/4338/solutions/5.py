def reverse_on_diagonals(mx):
    dl = []
    dr = []
    for i in range(len(mx)):
        dl.append(mx[i][i])
        dr.append(mx[i][-i - 1])
    for i in range(len(mx)):
        mx[i][i] = dl.pop()
        mx[i][-i - 1] = dr.pop()
    return mx
