def solution(string, ending):
    if ending:
        return ending == string[-1 * len(ending):]
    else:
        return True
