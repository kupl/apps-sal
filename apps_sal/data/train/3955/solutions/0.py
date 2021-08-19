def bracket_pairs(string):
    brackets = {}
    open_brackets = []
    for (i, c) in enumerate(string):
        if c == '(':
            open_brackets.append(i)
        elif c == ')':
            if not open_brackets:
                return False
            brackets[open_brackets.pop()] = i
    return False if open_brackets else brackets
