def chmod_calculator(perm):
    return str(sum([wbin(perm[k]) * {'user': 100, 'group': 10, 'other': 1}[k] for k in perm])).zfill(3)


def wbin(w):
    return int(w.translate(str.maketrans('rwx-', '1110')), 2)
