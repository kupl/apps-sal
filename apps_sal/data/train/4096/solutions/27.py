def valid_parentheses(string):
    counter = 0;
    for i in string:
        if i == "(": counter += 1
        if i == ")": counter -= 1
        if counter < 0: return(False)
    return(counter == 0)
