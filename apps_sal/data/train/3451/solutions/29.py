def triangle(array):
    n = len(array)
    colors = {"R": 0, "G": 1, "B": 2}
    digit = {0: "R", 1: "G", 2: "B"}
    a = [colors.get(item, item) for item in list(array)]

    # Generate nth the pascal's triangle row
    def pascalRowFast(rowIndex):
        row = [0] * (rowIndex + 1)
        row[0] = row[-1] = 1
        for i in range(0, rowIndex >> 1):
            x = row[i] * (rowIndex - i) // (i + 1)

            row[i + 1] = row[rowIndex - 1 - i] = x
        return row

    total = sum([a * b for a, b in zip(pascalRowFast(n - 1), a)]) * (-1)**(n - 1) % 3
    return digit[total]
