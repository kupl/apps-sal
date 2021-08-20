def solution(string, ending):
    if len(ending) == 0:
        return True
    if len(string) == 0:
        return False
    last1 = string[-1]
    last2 = ending[-1]
    if last1 == last2:
        return True and solution(string[:-1], ending[:-1])
    else:
        return False
