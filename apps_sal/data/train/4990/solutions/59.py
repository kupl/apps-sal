def solution(string, ending):
    l: int = len(ending)
    if l == 0:
        return True
    return string[-l:] == ending
