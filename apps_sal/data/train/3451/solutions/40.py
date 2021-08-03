colours = {"GG": "G", "BB": "B", "RR": "R", "BG": "R", "RG": "B", "BR": "G", "GB": "R", "GR": "B", "RB": "G"}


def triangle(row):
    while len(row) > 1:
        row_out = ""
        for i in range(0, len(row) - 1):
            row_out += colours[row[i:i + 2]]
        row = row_out
    print(row)
    return row
