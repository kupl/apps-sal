def triangle(row):
    dicts = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}
    if len(row) > 2:
        s = ''
        for i in range(len(row) - 1):
            s = s + dicts[row[i:i + 2]]
        row = s
        return triangle(row)
    elif len(row) > 1:
        return dicts[row]
    else:
        return row
