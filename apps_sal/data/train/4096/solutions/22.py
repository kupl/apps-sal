def valid_parentheses(string):
    depth = 0                           #Depth increases as we go 'deeper in parentheses', and decreases when parentheses are closed.
    for i in string:
        if i == "(":
            depth += 1
        elif i == ")":
            depth -= 1
        if depth < 0:
            return False                #If at some point depth becomes negative, we've met a situation, when the parentheses pair can't be closed - sequence is not valid
    if depth == 0:                      #At the end of valid sequence all opening parentheses' amount must be equal to the closing ones'.
        return True
    else:
        return False
