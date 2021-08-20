def getZarr(string):
    n = len(string)
    z = [0] * n
    (l, r, k) = (0, 0, 0)
    for i in range(1, n):
        if i > r:
            (l, r) = (i, i)
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


def zfunc(str_):
    solution = getZarr(str_)
    if len(solution) > 1:
        solution[0] = len(solution)
    return solution
