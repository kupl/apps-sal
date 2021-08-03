def valid_parentheses(string):
    string = "".join([x for x in string if x == "(" or x == ")"])
    before_reduce = len(string)
    string = string.replace('()', '')
    if string == '':
        return True
    elif before_reduce != len(string):
        return valid_parentheses(string)
    else:
        return False
