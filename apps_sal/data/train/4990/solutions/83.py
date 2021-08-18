def solution(string, ending):
    if(len(ending) == 0):
        return True

    length_ending = len(ending)
    length_start = len(string)
    if(string[length_start - length_ending:] == ending):
        return True
    else:
        return False
