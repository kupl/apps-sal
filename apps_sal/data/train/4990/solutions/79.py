def solution(string, ending):
    if (ending in string and ending == string[-len(ending):]) or ending == '':
        return True
    return False

