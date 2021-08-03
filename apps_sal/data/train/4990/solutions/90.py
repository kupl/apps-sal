def solution(string, ending):
    if ending == string[-len(ending):] or len(ending) == 0:
        return True
    return False
