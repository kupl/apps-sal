def get_mixed_num(fraction):
    arr = fraction.split('/')
    (a, b) = divmod(int(arr[0]), int(arr[1]))
    res = []
    if a != 0:
        res.append(str(a))
    if b != 0:
        res.append(str(b) + '/' + arr[1])
    return ' '.join(res)
