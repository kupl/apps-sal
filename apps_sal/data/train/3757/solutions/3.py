def round_to_five(l):
    return [round((0.01 + n) / 5) * 5 for n in l]
