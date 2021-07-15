def solve(s):
    indexes = []
    for i in range(len(s)):
        if s[i] == " ":
            indexes.append(i)
    lst = s.split(" ")
    result = []
    for i in range(len(lst)):
        result.append(lst[i][::-1])
    result.reverse()
    t = "".join(result)
    t = list(t)
    for i in range(len(indexes)):
        t.insert(indexes[i], " ")
    return "".join(t)

