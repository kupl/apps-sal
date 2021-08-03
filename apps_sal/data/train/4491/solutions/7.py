def solve(a, b):
    string = ""
    for i in a:
        if i not in b:
            string = string + i
    for i in b:
        if i not in a:
            string = string + i
    return string
