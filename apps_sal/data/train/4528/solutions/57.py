def maxindex(lst):
    maxnum = 0
    maxindex = 0
    for i in range(len(lst)):
        if lst[i] > maxnum:
            maxnum = lst[i]
            maxindex = i
    return maxindex

def my_languages(results):
    values = []
    keys = []
    ans = []
    for item in results:
        keys.append(item)
        values.append(results[item])
    for i in range(len(values)):
        index = maxindex(values)
        if values[index] >= 60:
            ans.append(keys[index])
            del values[index]
            del keys[index]
    return ans


