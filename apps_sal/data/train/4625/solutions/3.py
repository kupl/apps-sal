def processes(start, end, processes):
    if start == end:
        return []
    result = check(start, end, processes, [])
    if result == None:
        return []
    return result


def check(start, end, processes, result):
    if start == end:
        return result
    results = []
    for i in processes:
        if i[1] == start:
            try:
                tmp = result.copy()
                tmp.append(i[0])
                tmp2 = check(i[2], end, processes, tmp)
                if tmp2 != None:
                    results.append(tmp2)
            except:
                return None
    if len(results) > 0:
        return min(results, key=len)
    else:
        return None
