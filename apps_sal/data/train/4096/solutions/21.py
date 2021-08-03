def valid_parentheses(s):
    lvl = 0
    for c in s:
        lvl += (c == '(') - (c == ')')
        if lvl < 0:
            return False
    return not lvl
