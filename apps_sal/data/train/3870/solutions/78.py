def solve(s):
    sol = []
    l = []
    for i in range(len(s)):
        if (s[i] == " "):
            l.append(i)
        else:
            sol.append(s[i])
    sol.reverse()

    for i in range(len(l)):
        sol.insert(l[i], " ")
    return("".join(sol))
