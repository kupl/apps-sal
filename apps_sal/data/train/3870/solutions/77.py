def solve(s):
    spaces = []
    word = []
    for i in range(len(s)):
        if s[i] == " ":
            spaces.append(i)
        else:
            word.append(s[i])
    word = word[::-1]
    for i in spaces:
        word.insert(i, " ")
    var = ""
    return var.join(word)
