def solution(string, ending):
    if ending == string[-len(ending):len(string)] or ending == '':
        return True
    else:
        return False
