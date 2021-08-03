def solution(string, ending):
    if not ending:
        return True
    length = -len(ending)
    if string[length:] == ending:
        return True
    else:
        return False
