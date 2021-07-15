def count_by(x, n):
    res = []
    sum = 0
    for i in range(n):
        sum += x
        res.append(sum)
    return res
