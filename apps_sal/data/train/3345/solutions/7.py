def find_uniq(arr):
    S = ''.join(arr)
    D = {}
    for i in S:
        D[i] = D.get(i, 0) + 1
    L = sorted([(v, k) for (k, v) in list(D.items())], reverse=True)
    Minv = L[-1][0]
    Min = L[-1][1]
    for word in arr:
        if word.count(Min) >= Minv:
            return word
