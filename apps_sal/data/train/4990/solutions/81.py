def solution(string, ending):
    x = len(string) - len(ending)
    y = string[x:]
    if y == ending:
        return True
    else:
        return False
