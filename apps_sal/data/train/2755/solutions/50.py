def multiple_of_index(arr):
    temp=[]
    for n in range(1, len(arr)):
        if arr[n] % n == 0:
            temp.append(arr[n])
    return temp
