def min_sum(arr):
    arr = sorted(arr)
    arr1 = arr[::2]
    arr2 = arr[1::2][::-1]
    a = []
    for i in range(len(arr1)):
        a.append(arr1[i]*arr2[i])
    return sum(a)
        

