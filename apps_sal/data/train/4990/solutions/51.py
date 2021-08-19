def solution(string, ending):
    return True if ending == '' or string[-1 * len(ending):] == ending else False
