def solution(string, ending):
    negValue = 0 - len(ending)
    if ending == '':
        return True
    elif string[negValue:] != ending:
        return False
    else:
        return True
