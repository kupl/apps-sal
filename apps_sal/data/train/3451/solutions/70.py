C = {
    "GG": "G",
    "RR": "R",
    "BB": "B",
    "BG": "R",
    "GB": "R",
    "RG": "B",
    "GR": "B",
    "RB": "G",
    "BR": "G"
}


def triangle(row: str):
    tmp_row = []
    while len(row) != 1:
        for i in range(len(row) - 1):
            tmp_row.append(C.get(row[i:i + 2]))
        row = "".join(tmp_row)
        tmp_row.clear()
    return row[0]
