from statistics import mean

def max_sumDig(nMax, maxSum):
    def okay(x):
        L = list(map(int, str(x)))
        return all(sum(t) <= maxSum for t in zip(L, L[1:], L[2:], L[3:]))
    result = list(filter(okay, range(1000, nMax+1)))
    m = mean(result)
    return [len(result), min(result, key=lambda x:abs(x-m)), sum(result)]
