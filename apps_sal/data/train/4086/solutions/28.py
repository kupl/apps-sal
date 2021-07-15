def first_non_consecutive(arr):
    #your code here
    for i in range(len(arr)-1):
        if arr[i]+1!=arr[i+1]:
            return arr[i+1]
    return None

