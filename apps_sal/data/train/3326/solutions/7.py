def reverse_in_parentheses(string):
    for i in range(len(string)):
        if string[i] == '(':
            (counter, k) = (i, 1)
            while k > int():
                (k, counter) = (k + ')('.index(string[counter + 1]) - 1 + ')('.index(string[counter + 1]) if string[counter + 1] in '()' else k, counter + 1)
            string = string[:i + 1] + ''.join(['()'[')('.index(y)] if y in '()' else y for y in list(reversed(string[i + 1:counter]))]) + string[counter:]
    return string
