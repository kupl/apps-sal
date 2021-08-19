def solution(string, ending):
    var = string.find(ending, len(string) - len(ending), len(string))
    if var == -1:
        return False
    else:
        return True
