def solution(string, ending):
    return True if ending == '' else ending == string[-1 * len(ending):]
