def max_tri_sum(numbers):
    newList = []
    newList = list(set(numbers))
    newList.sort(reverse=True)
    result = newList[0] + newList[1] + newList[2]
    return result
