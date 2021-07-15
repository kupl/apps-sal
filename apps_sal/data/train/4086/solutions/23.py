def first_non_consecutive(arr):
    for x in range(1,len(arr)):
        if arr[x]-1 != arr[x-1]:
            return arr[x]

