def isValid(formula):
    #     print((1 in formula) != (2 in formula))
    return not ((1 in formula) and (2 in formula)) \
        and not ((3 in formula) and (4 in formula)) \
        and (5 in formula) == (6 in formula) \
        and ((7 in formula) or (8 in formula))
