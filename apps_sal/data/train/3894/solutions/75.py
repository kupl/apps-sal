def solve(s):
    case = 0
    for char in s:
        if char.isupper():
            case += 1
        else:
            case -= 1
    if case > 0:
        return s.upper()
    else:
        return s.lower()
