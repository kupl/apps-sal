def triangle(row):
    f = len(row)
    for i in range(f - 1):
        a = ""
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                a += row[i]
            else:
                a += "".join(set("RGB") - set(row[i]) - set(row[i + 1]))
        row = a[:]
    return row
