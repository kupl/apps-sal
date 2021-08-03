def solution(string, ending):
    if ending == '':
        return True
    return ending == string[len(string) - len(ending):]
