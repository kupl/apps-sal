def solution(string, ending):
    remove = len(string) - len(ending)
    return string[remove:] == ending
