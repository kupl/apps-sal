def find_longest(arr):
    arr = [str(i) for i in arr]
    L = len(max(arr,key=len))
    return int([i for i in arr if len(i) == L][0])
