def solve(s):
    without = [c for c in s if c != ' ']
    spaces = [i for i, e in enumerate(s) if e == ' ']
    rev = without[::-1]
    result = []
    j = 0
    for i in range(len(s)):
        if i in spaces:
            result.append(' ')
        else:
            result.append(rev[j])
            j += 1
    return "".join(result)
