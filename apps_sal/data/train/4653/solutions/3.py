table = {o + c: c + (o + 1) % 26 for c in (97, 65) for o in range(26)}


def next_letter(stg):
    return stg.translate(table)
