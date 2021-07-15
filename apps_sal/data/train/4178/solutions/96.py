def min_sum(arr):
    arr.sort()
    list_sum = []
    while len(arr) > 0:
        min_index = 0
        max_num = arr.pop()
        min_num = arr.pop(min_index)
        min_index += 1
        list_sum.append(max_num * min_num)
    return sum(list_sum)
