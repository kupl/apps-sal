def solution(string, ending):
    if not string:
        return False
    elif not ending or string == ending:
        return True
    return solution(string[1:], ending)
