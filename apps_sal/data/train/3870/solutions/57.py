def solve(s):
    spaces = [i for i, letter in enumerate(s) if letter == " "]
    s = list(s)
    for i in range(len(spaces)-1 ,-1,-1):
        s.pop(spaces[i])
    srev = s[::-1]
    for i in range(0, len(spaces) ):
        srev.insert(spaces[i], " ")
    final = ""
    for z in srev:
        final = final + z
    return final
