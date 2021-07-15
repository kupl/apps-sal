def solution(string, ending):
    a=string[len(string)-len(ending):]
    if (a==ending):
        return True
    else:
        return False
