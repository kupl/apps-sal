def count_sel(lst):
    dic = {}
    result = []
    arr_temp = []
    for elm in lst:
        if elm not in dic:
            dic[elm] = 1
        else:
            dic[elm] += 1
    result.append(len(lst))
    result.append(len(dic.keys()))
    result.append(list(dic.values()).count(1))
    for (elm, occurrence) in dic.items():
        if occurrence == max(dic.values()):
            arr_temp.append(elm)
    result.append([sorted(arr_temp), max(dic.values())])
    return result
