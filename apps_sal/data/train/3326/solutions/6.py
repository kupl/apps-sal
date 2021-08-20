def reverse_in_parentheses(string):
    for i in range(len(string)):
        if string[i] == '(':
            (walker, depth) = (i, 1)
            while depth > int():
                (depth, walker) = (depth + ')('.index(string[walker + 1]) - 1 + ')('.index(string[walker + 1]) if string[walker + 1] in '()' else depth, walker + 1)
            string = string[:i + 1] + ''.join(['()'[')('.index(y)] if y in '()' else y for y in list(reversed(string[i + 1:walker]))]) + string[walker:]
    return string
