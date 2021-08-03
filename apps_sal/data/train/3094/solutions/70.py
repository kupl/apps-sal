def sum_array(arr):

    if arr == None or int(len(arr)) <= 2:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))

        #new_list = [x for x in arr if x != max(arr) or min(arr)]
        return sum(arr)
