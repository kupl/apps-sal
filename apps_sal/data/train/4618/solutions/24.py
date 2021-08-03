def positive_sum(arr):
    positive_list = []
    for num in arr:
        if num >= 0:
            positive_list.append(num)
    result = sum(positive_list)
    return result
