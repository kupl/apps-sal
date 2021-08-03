def solution(a, b):
    if len(a) > len(b):
        return str(b) + str(a) + str(b)
    elif len(a) < len(b):
        return str(a) + str(b) + str(a)
    else:
        return 'Error'
