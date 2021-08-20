colorReverDic = {'RR': 'R', 'RG': 'B', 'RB': 'G', 'GG': 'G', 'GR': 'B', 'GB': 'R', 'BB': 'B', 'BR': 'G', 'BG': 'R'}


def triangle(row):
    newRow = row
    for i in range(len(row) - 1):
        l = len(newRow) - 1
        workRow = ''
        for c in range(l):
            workRow += colorReverDic[newRow[c] + newRow[c + 1]]
        newRow = workRow
    return newRow
