def max_sumDig(nMax, maxSum):

    def isGood(s):
        return all((sum(map(int, str(s[i:i + 4]))) <= maxSum for i in range(len(s) - 3)))
    lst = [n for n in range(1000, nMax + 1) if isGood(str(n))]
    (s, l) = (sum(lst), len(lst))
    avg = 1.0 * s / l
    iAvg = next((i for (i, n) in enumerate(lst) if n > avg))
    nearest = sorted(lst[iAvg - 1:iAvg + 1], key=lambda n: abs(n - avg))[0]
    return [l, nearest, s]
