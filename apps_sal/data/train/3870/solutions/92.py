def solve(s):
    a = [i for i in "".join(s[::-1].split())]
    for i in range(len(s)):
        if s[i] == " ":
            a.insert(i, " ")
    return "".join(a)
