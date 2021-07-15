def solution(str, ending):
    if len(ending) == 0 or ending == str[-len(ending):]:
        return True
    return False
