def insert_space(s, res):
    res = list(res)
    for i in range(len(s)):
        if(s[i] == " "):
            res.insert(i, " ")
    return "".join(res)

def solve(s):
    temp = s.translate({ord(" "):None})
    res = temp[::-1]
    return insert_space(s, res)

