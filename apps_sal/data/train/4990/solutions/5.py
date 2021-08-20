def solution(string, ending):
    return ending == string[len(string) - len(ending):]
