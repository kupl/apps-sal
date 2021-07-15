def solution(string, ending):
    if len(string) < len(ending):
        return False
    for i in range(len(ending)):
        if string[-i - 1] != ending[-i - 1]:
            return False
    return True
