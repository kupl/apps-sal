def find_longest(arr):
    a = max(arr)
    for i in range(len(arr)):
        if len(str(arr[i])) == len(str(a)):
            return arr[i]
