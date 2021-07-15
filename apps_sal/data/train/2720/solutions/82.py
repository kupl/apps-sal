def solution(d):
    return max([int(d[x:x+5]) for x in range(len(d)-4)])
