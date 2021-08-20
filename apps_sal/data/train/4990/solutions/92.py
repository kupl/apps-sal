def solution(string, ending):
    return True if string[len(string) - len(ending):len(string) + 1] == ending else False
