def solution(string, ending):
    firstsymbol = len(string) - len(ending)
    podstroka = string[firstsymbol:]
    if podstroka == ending:
        return True
    else:
        return False
