def binary_array_to_number(arr):
    res = 0
    li = [x for x in reversed(arr)]
    print(li)
    for i in range(len(li)):
        if li[i] == 1:
            res = res + 2 ** i
    return res
