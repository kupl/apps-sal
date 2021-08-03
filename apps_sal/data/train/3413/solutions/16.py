def solution(n, q=[]):
    if n == None:
        return q
    o = []
    for i in n:
        o += chr(i)
        o.sort()
    p = []
    for i in o:
        p.append(ord(i))
    return p
