repls = {
    "RR": "R",
    "GG": "G",
    "BB": "B",

    "GB": "R",
    "BR": "G",
    "RG": "B",

    "BG": "R",
    "RB": "G",
    "GR": "B",
}


def reduce1(row):
    return ''.join(repls[row[i:i + 2]] for i in range(len(row) - 1))


def triangle(row):
    while len(row) > 1:
        row = reduce1(row)
    return row
