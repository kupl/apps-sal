def solution(string):
    out = []
    for i in string:
        out.insert(-1 - string.index(i), i)
    return ''.join(out)
