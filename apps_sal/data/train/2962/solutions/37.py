def divisible_by(num, div):
    res = []
    i = 0
    while i < len(num):
        if num[i] % div == 0:
            res.append(num[i])
        i += 1

    return res
