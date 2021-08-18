def solution(string):
    res = ''
    flip = list(string)

    while len(flip) > 0:
        res += flip.pop()

    return res
