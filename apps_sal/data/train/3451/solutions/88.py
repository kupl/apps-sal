def triangle(row):
    for i in range(0, len(row) - 1):
        res = []
        for k in range(0, len(row) - 1):
            if row[k] == row[k + 1]:
                res += row[k]
            else:
                res += 'GBR'.replace(row[k], '').replace(row[k + 1], '')
        row = res
    return row[0]
    pass
