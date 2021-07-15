def solution(x):
    v = 99999
    while v > 0:
        if str(v) in str(x):
            return v
        v = v - 1
