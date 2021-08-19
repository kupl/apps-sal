def solution(a, b):
    l = []
    (l.append(a), l.append(b))
    l.sort(key=lambda x: len(x))

    def res(x):
        return f'{x[0]}{x[1]}{x[0]}'
    return res(l)
