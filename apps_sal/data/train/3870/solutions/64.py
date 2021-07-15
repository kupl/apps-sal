def solve(s):
    spaces = [i for i, c in enumerate(s) if c == " "]
    string = list(s.replace(" ", "")[::-1])
    for space in spaces:
        string.insert(space, " ")
    return "".join(string)
