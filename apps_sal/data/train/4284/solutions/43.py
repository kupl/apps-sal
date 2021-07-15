def array_leaders(numbers):
    lsum = 0
    res = []
    tsum = sum(numbers)
    for i in numbers:
        lsum += i
        if i > tsum - lsum:
            res.append(i)
    return res
