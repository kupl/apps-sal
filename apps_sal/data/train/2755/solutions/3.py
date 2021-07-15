def multiple_of_index(arr):
    i = 1
    rst = []
    while i < len(arr):
        if arr[i] % i == 0:
            print(i)
            rst.append(arr[i])
        i += 1
    return rst
