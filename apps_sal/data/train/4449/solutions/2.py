def solution(s):
    r = s
    for i in range(9):
        r = r.replace('RR', 'R').replace('GG', 'G').replace('BB', 'B')
    return len(s) - len(r)
