def black_and_white(height, width, compressed):
    r = []
    row = []
    for i, x in enumerate(compressed):
        color = i % 2
        if not row and color:
            row.append(0)
        remain = width - sum(row)
        if x > remain:
            row.append(remain)
            if len(row) % 2 == 1:
                if row[-1] == 0:
                    row.pop()
                else:
                    row.append(0)
            r.append(row)
            x = x - remain
            while(x >= width):
                if color:
                    r.append([0, width])
                else:
                    r.append([width, 0])
                x -= width
            if color:
                row = [0, x]
            else:
                row = [x]
        else:
            row.append(x)
    if row:
        if len(row) % 2 == 1:
            if row[-1] == 0:
                row.pop()
            else:
                row.append(0)
        r.append(row)
    if r[-1] == [0, 0]:
        r.pop()
    return r
