def pascal(p):
    (row, res) = ([1], [])
    for x in range(max(p, 0)):
        res.append(row)
        row = [l + r for (l, r) in zip(row + [0], [0] + row)]
    return res
