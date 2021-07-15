def solution(string, ending):
    a = len(ending)
    b = len(string)
    if string[b-a:b] == ending:
        return True
    else:
        return False
