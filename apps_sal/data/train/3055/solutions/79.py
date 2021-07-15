def sum_str(a, b):
    bs = [a, b]
    sum = 0
    for i in bs:
        try:
            value = int(i)
        except:
            value = 0
        sum += value
    return str(sum)
