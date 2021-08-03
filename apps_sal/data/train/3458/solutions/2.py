def multiplication_table(row, col):
    res = []
    for i in range(1, row + 1):
        item = []
        for j in range(1, col + 1):
            item.append(i * j)
        res.append(item)
    return res
