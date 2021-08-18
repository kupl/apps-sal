def valid_parentheses(string):

    open = 0

    for c in string:

        if c == "(":
            open += 1

        elif c == ")":
            open -= 1

        if open < 0:
            return False

    return open == 0
