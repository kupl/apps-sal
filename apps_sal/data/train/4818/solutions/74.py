def solution(a, b):
    string = ''
    if len(a) > len(b):
        string += b
        string += a
        string += b
    else:
        string += a
        string += b
        string += a
    return string
