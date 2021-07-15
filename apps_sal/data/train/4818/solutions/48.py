def solution(a, b):
    la = len(a)
    lb = len(b)
    shrt = a
    lng = b
    if la>lb:
        shrt = b
        lng = a
    return shrt+lng+shrt

