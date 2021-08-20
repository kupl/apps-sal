def solution(string, ending):
    if ending == '' or (len(string) > 0 and len(ending) > 0 and (ending in string) and (ending[-1] == string[-1])):
        return True
    else:
        return False
