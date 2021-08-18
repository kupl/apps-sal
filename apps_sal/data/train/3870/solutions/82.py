def solve(s):
    no_space = list(s.replace(" ", "")[::-1])
    for i in [pos for pos, char in enumerate(s) if char == " "]:
        no_space.insert(i, " ")
    return ''.join(no_space)
