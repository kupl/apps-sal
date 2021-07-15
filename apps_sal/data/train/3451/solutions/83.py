cash = {
    "R": "R",
    "G": "G",
    "B": "B",
    "RR": "R",
    "RG": "B",
    "RB": "G",
    "GR": "B",
    "GG": "G",
    "GB": "R",
    "BR": "G",
    "BG": "R",
    "BB": "B"
}


def triangle(row):
    result = cash.get(row, False)
    if not result:
        result = cash[triangle(row[:-1]) + triangle(row[1:])]
        cash.update({row: result})
        return result
    return result
