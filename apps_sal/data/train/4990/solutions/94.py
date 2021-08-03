def solution(string, ending):
    s = len(string)
    e = len(ending)
    if string[:-e] + ending == string:
        return True
    if ending == '':
        return True
    return False
