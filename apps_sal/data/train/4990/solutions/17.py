def solution(string, ending):
    if len(ending) > len(string):
        return False
    elif ending == '':
        return True
    else:
        for (x, y) in zip(string[::-1], ending[::-1]):
            if x != y:
                return False
    return True
