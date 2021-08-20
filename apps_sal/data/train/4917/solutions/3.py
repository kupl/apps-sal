BRACES = {'(': ')', '{': '}', '[': ']'}


def validBraces(string):
    waiting = []
    for l in string:
        if l in BRACES.keys():
            waiting.append(BRACES[l])
        elif not waiting or waiting.pop() != l:
            return False
    return not waiting
