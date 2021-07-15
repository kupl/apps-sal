def solution(a, b):
    string = ''
    if len(a)>len(b):
        string = b + a + b
    else:
        string = a + b + a
    return string
