try:
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))
    out = list(map(sorted, arr))
    dic = {}
    for elem in out:
        dic.setdefault(tuple(elem), list()).append(1)
    for (k, v) in list(dic.items()):
        dic[k] = sum(v)
    unique_set = 0
    for v in list(dic.values()):
        if v == 1:
            unique_set += 1
    print(unique_set)
except:
    pass
