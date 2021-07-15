def solution(string, ending):
    length = len(ending)
    if ending == '':
        return True
    else:
        if string[-length : ] == ending:
            return True
        return False
