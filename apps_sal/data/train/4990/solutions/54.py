def solution(string, ending):
    if ending == '':
        return True
    else:
        end_len = -1 * len(ending)
        return string[end_len:] == ending
