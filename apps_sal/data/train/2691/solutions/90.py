def solve(s):
    res = []
    temp = list(s)
    max = 0
    for item in temp:
        if item.isalpha():
            res.append(' ')
        else:
            res.append(item)
    res = ''.join(res).split(' ')
    for item in res:
        if item != '' and int(item) > max:
            max = int(item)
    return max
