def solve(arr):

    def isProgression(array):
        prevstep = array[1] - array[0]
        for (j, v) in enumerate(array[1:]):
            curstep = array[j + 1] - array[j]
            if curstep != prevstep:
                return False
            prevstep = curstep
        return True
    if isProgression(arr):
        return 0
    lst = [arr]
    chg = [0]
    good = [isProgression(arr)]
    for j in range(len(arr)):
        for k in range(len(lst)):
            if j > 2 and isProgression(lst[k][:j - 1]) is not True:
                continue
            lstp1 = lst[k][:j] + [lst[k][j] + 1] + lst[k][j + 1:]
            lst.append(lstp1)
            chg.append(chg[k] + 1)
            good.append(isProgression(lstp1))
            lstm1 = lst[k][:j] + [lst[k][j] - 1] + lst[k][j + 1:]
            lst.append(lstm1)
            chg.append(chg[k] + 1)
            good.append(isProgression(lstm1))
    filtered_lst = [x for (j, x) in enumerate(lst) if good[j]]
    filtered_chg = [x for (j, x) in enumerate(chg) if good[j]]
    if len(filtered_lst) == 0:
        return -1
    return min(filtered_chg)
