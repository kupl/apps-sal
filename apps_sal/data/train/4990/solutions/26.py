def solution(string, ending):
    comparison = string[-len(ending):]
    if len(ending) == 0:
        return True
    if comparison == ending:
        return True
    else:
        return False
