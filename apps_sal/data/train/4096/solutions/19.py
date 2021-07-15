def valid_parentheses(string):
    count = 0
    for c in [c for c in string if c in "()"]:
        count += 1 if c == '(' else -1
        if count < 0:
            return False
    return count == 0
