def solve(arr):
    arr.sort()
    
    while len(arr) >= 1:
        if arr[0] < 0 and abs(arr[0]) in arr:
            x = abs(arr[0])
            arr.remove(arr[0])
            arr.remove(x)
        else:
            return arr[0]
