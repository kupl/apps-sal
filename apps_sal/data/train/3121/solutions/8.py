def solve(arr):
    summa = 0
    dic = {}
    res = 0
    for i in arr:
        dic[i] = 0
        if -i in arr:
            dic[i] += 1
        else:
            dic[i] = 0
    for key, value in dic.items():
        if value == 0:
            res = key
    return res
