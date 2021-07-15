def solution(string):
    a = list()
    for i in string:
        a.append(i)
    a.reverse()
    c = str()
    for v in a:
        c = c + v
    return c
