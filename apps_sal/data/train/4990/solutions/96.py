def solution(string, ending):
    if len(ending) > len(string):
        return False
    i = -1
    len_str = len(ending)
    while i >= -len_str:
        if ending[i] != string[i]:
            return False
        i += -1
    return True
