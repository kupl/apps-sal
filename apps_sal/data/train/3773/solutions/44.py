def isValid(formula):
    rules = [not(1 in formula and 2 in formula)]
    rules.append(not(3 in formula and 4 in formula))    
    rules.append((5 in formula and 6 in formula) or (5 not in formula and 6 not in formula))
    rules.append(7 in formula or 8 in formula)
    print(rules)
    return all(rules)
