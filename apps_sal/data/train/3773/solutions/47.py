def isValid(formula=[1, 3, 7]):
    fr = not (1 in formula and 2 in formula)
    sr = not (3 in formula and 4 in formula)
    tr = not((5 in formula and 6 not in formula) or (5 not in formula and 6 in formula))
    four = (7 in formula or 8 in formula)
    return fr and sr and tr and four
