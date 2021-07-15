def isValid(formula):
    rule_1 = 1 not in formula or 2 not in formula
    rule_2 = 3 not in formula or 4 not in formula
    rule_3 = 5 in formula and 6 in formula or 5 not in formula and 6 not in formula
    rule_4 = 7 in formula or 8 in formula
    return rule_1 and rule_2 and rule_3 and rule_4
