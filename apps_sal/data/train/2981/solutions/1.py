def solution(n,d):
    s = str(n)
    return list(map(int,s))[-d if d>0 else len(s):]
