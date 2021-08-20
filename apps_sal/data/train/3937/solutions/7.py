def x(i, maxSum):
    s = str(i)
    for i in range(len(s) - 3):
        if sum(map(int, list(s[i:i + 4]))) > maxSum:
            return False
    return True


def max_sumDig(nMax, maxSum):
    count = 0
    sum_ = 0
    mean_ = 0
    _3 = None
    for i in range(1000, nMax + 1):
        if x(i, maxSum):
            count += 1
            sum_ += i
            if not _3:
                _3 = i
    mean_ = float(sum_) / count
    _3 = i
    for i in range(1000, nMax + 1):
        if x(i, maxSum):
            if abs(i - mean_) < abs(_3 - mean_):
                _3 = i
    return [count, _3, sum_]
