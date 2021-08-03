def triangle(row):
    def add(c1, c2):
        return c1 if c1 == c2 else "RGB".replace(c1, "").replace(c2, "")

    while len(row) > 1:
        s = ""
        for i in range(0, len(row) - 1):
            s += add(row[i], row[i + 1])
        row = s
    return row
