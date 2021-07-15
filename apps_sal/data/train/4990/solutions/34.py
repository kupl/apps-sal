def solution(string, ending):
    size = len(ending)
    if string[-size:] == ending or ending == '':
        return True
    else:
        return False
    pass
