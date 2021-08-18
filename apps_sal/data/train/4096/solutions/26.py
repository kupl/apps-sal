
def valid_parentheses(string):
    str = string
    if str == "":
        return True
    if len(str) > 100:
        str = str[0:100]
    c_open = 0
    exc = 0
    for c in str:
        if c == '(':
            c_open += 1
        if c == ')':
            c_open -= 1
            if c_open < 0:
                exc = 1
                break
    if exc == 1 or c_open != 0:
        return False
    return True
