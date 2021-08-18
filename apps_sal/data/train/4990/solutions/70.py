def solution(string, ending):
    if len(ending) == 0:
        return True
    if string and string[-len(ending):] == ending:
        return True
    else:
        return False
