def triangle(row):
    to_num = {'R': 1, 'G': 2, 'B': 3}
    from_num = {1: 'R', 2: 'G', 3: 'B'}

    row_num = [to_num[y] for y in row]

    while(len(row_num) > 1):
        t = []
        for x in range(len(row_num) - 1):
            if row_num[x] == row_num[x + 1]:
                t.append(row_num[x])
            else:
                t.append(6 - row_num[x] - row_num[x + 1])
        row_num = t

    return from_num[row_num[0]]
