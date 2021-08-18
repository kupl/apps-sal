def triangle(row):
    if len(row) == 1:
        return row
    else:
        new_row = ''
        for a, b in zip(row[:-1], row[1:]):
            if a == b:
                new_row += a
            else:
                for letter in "RGB":
                    if letter not in (a, b):
                        new_row += letter
                        break
        return triangle(new_row)
