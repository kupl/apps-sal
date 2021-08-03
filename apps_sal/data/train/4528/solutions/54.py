def indexmax(lst):  # returns the index of a max element
    maxval = 0
    maxindex = 0
    for i in range(len(lst)):
        if lst[i] > maxval:
            maxval = lst[i]
            maxindex = i
    return maxindex


def my_languages(results):
    keys = []
    values = []
    result_ans = []

    for result in results:
        keys.append(result)
        values.append(results[result])

    for i in range(len(keys)):
        index = indexmax(values)
        if values[index] >= 60:
            result_ans.append(keys[index])
            del keys[index]
            del values[index]

    return result_ans
