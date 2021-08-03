def find_longest(arr):
    result = str(arr[0])
    print(result)
    for i in range(len(arr)):
        if len(str(arr[i])) > len(result):
            result = str(arr[i])
    return int(result)
