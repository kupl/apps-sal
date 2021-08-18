def solve(s):
    space_index = [i for i in range(len(s)) if s[i] == " "]
    s = ''.join(s.split())
    s = s[::-1]
    for i in space_index:
        s = s[:i] + " " + s[i:]
    return s
