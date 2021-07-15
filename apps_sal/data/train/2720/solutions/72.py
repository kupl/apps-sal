def solution(d):
    s = str(d)
    return max([int(s[i:i+5]) for i in range(len(s)-4)])

