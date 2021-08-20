def find_longest(arr):
    string_array = [str(num) for num in arr]
    max_length = -1
    for ele in string_array:
        if len(ele) > max_length:
            max_length = len(ele)
            result = ele
    return int(result)
