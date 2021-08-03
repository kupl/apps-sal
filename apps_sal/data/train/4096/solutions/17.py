def valid_parentheses(string):

    open = 0

    for c in string:

        # increase open count for an open parenthesis
        if c == "(":
            open += 1

        # descrease open count for a closing parenthesis
        elif c == ")":
            open -= 1

        # if the open count ever drops below zero, parentheses are invalid
        if open < 0:
            return False

    # if open ends up non-zero, this returns False, otherwise True
    return open == 0
