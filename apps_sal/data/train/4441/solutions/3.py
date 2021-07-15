from functools import partial

trans = str.maketrans("rwx-", "1110")
base2 = partial(int, base=2)

def chmod_calculator(perm):
    return "{}{}{}".format(*map(base2, (perm.get(k, '---').translate(trans) for k in ("user", "group", "other"))))
