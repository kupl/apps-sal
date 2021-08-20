def multiple_of_index(arr):
    new_arr = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            new_arr.append(arr[i])
    return new_arr


'    new_arr = []\n    for i in range(1,len(arr)):\n        if (arr[i] % i == 0):\n            new_arr = \n        i = i + 1\n    return new_arr\n'
