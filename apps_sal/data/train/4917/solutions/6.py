def validBraces(string):
    stack = []
    delim = {'(':')', '[':']', '{':'}'}
    for c in string:
        if c in list(delim.keys()): stack.append(c)
        elif c in list(delim.values()):
            if not stack or delim[stack.pop()] != c: return False
    return not stack

