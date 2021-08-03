from itertools import combinations


def sat(f: Formula):

    literals = set()
    allLiterals(f, literals)
    all_lit = list(literals)
    for i in range(0, len(all_lit) + 1):
        lit_comb = set(combinations(all_lit, i))
        for j in lit_comb:
            if evaluate(f, j):
                return set(j)
    return False


def evaluate(f: Formula, inter):

    if f.is_literal():
        if f in inter:
            return True
        else:
            return False
    elif f.is_and():
        flag = True
        for i in f.args:
            flag = flag and evaluate(i, inter)
        return flag
    elif f.is_or():
        flag = False
        for i in f.args:
            flag = flag or evaluate(i, inter)
        return flag
    else:
        return (not evaluate(f.args[0], inter))


def allLiterals(f: Formula, lit_set):

    for i in f.args:
        if i.is_literal():
            lit_set.add(i)
        else:
            allLiterals(i, lit_set)
