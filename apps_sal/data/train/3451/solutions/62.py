def triangle(row):

    reduction = [3**i + 1 for i in range(10) if 3**i <= 100000][::-1]

    for j in reduction:

        while len(row) >= j:

            row = [row[i] if row[i] == row[i + j - 1] else ({"R", "G", "B"} - {row[i], row[i + j - 1]}).pop() for i in range(len(row) - j + 1)]

    return row[0]
