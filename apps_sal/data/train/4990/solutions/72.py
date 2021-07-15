def solution(string, ending):
    x = len(ending)
    string_end = string[-x:len(string) + 1]
    if len(ending) == 0:
        return True
    elif string_end == ending:
        return True
    else:
        return False
