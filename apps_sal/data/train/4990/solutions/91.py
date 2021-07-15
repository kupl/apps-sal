def solution(string, ending):
    if string[-len(ending):] == ending:
        return True
    elif len(ending) == 0:
        return True
    return False
