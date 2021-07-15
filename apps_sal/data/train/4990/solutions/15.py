def solution(string, ending):
    if ending not in string or len(ending) > 0 and string[-1] != ending[-1]:
        return False
    else:
        return True
