def valid_parentheses(string):

    count_open = 0
    count_close = 0

    index_open = 0
    index_closed = 0
    for s in string:
        if s == "(":
            count_open += 1
        elif s == ")":
            count_close += 1

            if count_close > count_open:
                return False

    if (count_open != count_close):
        return False
    else:
        return True
