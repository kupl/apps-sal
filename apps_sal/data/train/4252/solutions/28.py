def merge_arrays(first, second):
    i = 0
    j = 0
    print(first, second)
    common = []
    output = []
    if first == second and first == []:
        return []
    if first == []:
        return second
    if second == []:
        return first
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            common.append(first[i])
            i = i + 1
        elif first[i] == second[j]:
            common.append(first[i])
            i = i + 1
            j = j + 1
        elif first[i] > second[j]:
            common.append(second[j])
            j = j + 1
    if i < len(first):
        for k in range(i, len(first)):
            common.append(first[k])
    if j < len(second):
        for k in range(j, len(second)):
            common.append(second[k])
    output = [common[0]]
    k = 0
    for i in range(1, len(common)):
        if output[k] != common[i]:
            output.append(common[i])
            k = k + 1
    return output
