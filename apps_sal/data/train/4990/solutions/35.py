def solution(string, ending):
    e_len = len(ending)
    s_len = len(string)
    if e_len == 0:
        return True
    elif (s_len >= e_len) and (string[-e_len:] == ending):
        return True
    else:
        return False
