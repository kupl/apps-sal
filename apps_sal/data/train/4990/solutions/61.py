def solution(string, ending):

    if(string[-len(ending):]==ending or string == ending or ending == ''):
        return True
    else:
        return False
    pass
