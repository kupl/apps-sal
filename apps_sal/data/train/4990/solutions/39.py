def solution(string, ending):
    a = string.find(ending, len(string) - len(ending))
    if a != -1:
        return True
    else:
        return False
