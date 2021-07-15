def find_longest(arr):
    max = len(str(arr[0]))
    max_a = arr[0]
    for a in arr:
        print(a)
        if len(str(a)) > max:
            max = len(str(a))
            max_a = a
            
    return max_a
