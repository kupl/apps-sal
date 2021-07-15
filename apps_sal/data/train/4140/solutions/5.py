def bubblesort_once(arr):

    new_arr = arr.copy()
    for i in range(len(new_arr)-1):
        if new_arr[i]>new_arr[i+1]:
            new_arr[i], new_arr[i+1] = new_arr[i+1], new_arr[i]
    return new_arr
