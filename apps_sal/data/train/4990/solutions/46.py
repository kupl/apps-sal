def solution(string, ending):
    index = string.rfind(ending)
    if (index == len(string) - len(ending) or not ending) and index >= 0: return True
    else: return False

