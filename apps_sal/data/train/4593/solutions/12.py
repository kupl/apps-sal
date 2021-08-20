def merge_arrays(arr1, arr2):
    arr1 = [arr1, arr1[::-1]][arr1[0] < arr1[-1]]
    arr2 = [arr2, arr2[::-1]][arr2[0] < arr2[-1]]
    res = len(arr1) + len(arr2)
    new = []
    while len(new) < res:
        if arr1 and arr2:
            if arr1[-1] < arr2[-1]:
                item = arr1.pop()
            else:
                item = arr2.pop()
        elif arr1:
            item = arr1.pop()
        elif arr2:
            item = arr2.pop()
        else:
            break
        if item not in new:
            new.append(item)
    return new
