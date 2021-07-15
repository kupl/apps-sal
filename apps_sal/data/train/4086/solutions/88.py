def first_non_consecutive(arr):
    i = 0
    j = 1
    for k in range(len(arr)-1):
        if arr[i] +1 != arr[j]:
            return arr[j]
        else:
            i += 1
            j+= 1
