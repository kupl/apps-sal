def vert_mirror(strng):
    subStrings = strng.split('\n')
    reversedStrings = [substring[::-1] for substring in subStrings]
    joinedStrings = '\n'.join(reversedStrings)
    return joinedStrings


def hor_mirror(strng):
    subStrings = strng.split('\n')
    reversedStrings = [substring for substring in reversed(subStrings)]
    joinedStrings = '\n'.join(reversedStrings)
    return joinedStrings


def oper(fct, s):
    return fct(s)
