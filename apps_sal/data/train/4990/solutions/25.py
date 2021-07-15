def solution(string, ending):
    l_ending = -(len(ending))
    if l_ending == 0:
        return True
    elif string[l_ending:] == ending:
        return True
    else:
        return False
