import re
def how_many_bees(b):
    if b is None:return 0
    new_temp = [[j for j in i] for i in b]
    c = [len(re.findall(r"bee", "".join(i+[' ']+i[::-1]))) for i in new_temp]+[ len(re.findall(r"bee", "".join(i+tuple(' ')+i[::-1]))) for i in zip(*new_temp)]
    return sum(c)
