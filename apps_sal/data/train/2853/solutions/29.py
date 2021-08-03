def solve(arr):
    num = 0
    while num < len(arr):
        counter = 0
        for elem in arr:
            if arr[num] == elem:
                counter += 1
        if counter > 1:
            del arr[num]
        else:
            num += 1
    return(arr)
