def find_array(arr1, arr2):
    arr = []
    try:
        for i in arr2:
            if len(arr1) == 0 or len(arr2) == 0:
                return []
            else:    
                arr.append(arr1[i])
    except IndexError:
        return arr
    return arr

