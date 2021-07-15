def solution(string, ending):
    length = len(ending)
    if string[len(string) - length:] == ending:
        return True
    else:
        return False
