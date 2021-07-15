
def indexmax(lst): #returns the index of the maximum element
    maxval = 0
    maxindex = 0
    for i in range(len(lst)):
        if lst[i]>maxval:
            maxval = lst[i]
            maxindex = i
    return maxindex


def my_languages(results):
    keys = []
    values = []
    resultans = []
    for result in results:
        keys.append(result)
        values.append(results[result])
    for i in range(len(keys)):
        index = indexmax(values)
        if values[index]>=60:
            resultans.append(keys[index])
            del keys[index]
            del values[index]
    return resultans
