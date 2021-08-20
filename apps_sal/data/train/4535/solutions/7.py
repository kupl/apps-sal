def zfunc(str_):
    if not str_:
        return []
    N = len(str_)
    Z = [N] + [0] * (N - 1)
    right = 0
    left = 0
    for i in range(1, N):
        if i > right:
            n = 0
            while n + i < N and str_[n] == str_[n + i]:
                n += 1
            Z[i] = n
            if n > 0:
                left = i
                right = i + n - 1
        else:
            p = i - left
            q = right - i + 1
            if Z[p] < q:
                Z[i] = Z[p]
            else:
                j = right + 1
                while j < N and str_[j] == str_[j - i]:
                    j += 1
                Z[i] = j - i
                left = i
                right = j - 1
    return Z
