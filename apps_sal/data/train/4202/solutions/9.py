def ulam_sequence(U,V,Q) :
    R = [U,V]
    S = [U + V]
    while len(R) < Q :
        while 1 < len(S) and S[-1] == S[-2] :
            T = S.pop()
            while T == S[-1] : S.pop()
        T = S.pop()
        S.extend(T + V for V in R)
        R.append(T)
        S.sort(reverse = True)
    return R
