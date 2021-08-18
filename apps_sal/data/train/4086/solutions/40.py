def first_non_consecutive(arr):
    length = len(arr)
    if length <= 2:
        return None
    len_list = list(range(length))
    for item in len_list:
        try:
            if abs(arr[item + 1] - arr[item]) != 1:
                return arr[item + 1]
                break
        except:
            return None
