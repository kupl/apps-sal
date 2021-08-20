def solution(string, ending):
    len_1 = len(ending)
    if ending == string[-len_1:] or ending == '':
        return True
    return False
