def solution(string, ending):
    A = False
    if ending == '':
        A = True
    elif string[-len(ending)::1] == ending:
        A = True
    return A
