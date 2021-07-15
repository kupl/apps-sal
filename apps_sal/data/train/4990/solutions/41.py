def solution(string, ending):
    str_len = len(string)
    end_len = len(ending)
    return str_len >= end_len and string[str_len - end_len:] == ending
