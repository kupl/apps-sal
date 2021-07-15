def solution(a, b):
    l = []
    l.append(a), l.append(b)
    l.sort(key=lambda x: len(x))
    res = lambda x: f"{x[0]}{x[1]}{x[0]}"
    return res(l)

