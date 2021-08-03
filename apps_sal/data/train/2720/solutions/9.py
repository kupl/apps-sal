def solution(d):
    return int(max([d[j:j + 5]] for j in [i for i in range(len(d)) if d[i] == max(d)])[0])
