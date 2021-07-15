def solution(string, ending):
    if ending in string[-len(ending):]:
        return True
    else:
        return False
