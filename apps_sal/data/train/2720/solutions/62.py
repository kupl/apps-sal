def solution(digits):
    d = str(digits)
    n = 0
    for x in range(0, len(d)-4):
        if int(d[x:x+5]) > n:
            n = int(d[x:x+5])
    return n
