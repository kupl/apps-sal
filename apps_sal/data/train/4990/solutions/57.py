def solution(string, ending):
    negValue = 0 - len(ending)
    if ending == '':
        return True
    else:
        if string[negValue:] != ending:
            return False
        else:
            return True
