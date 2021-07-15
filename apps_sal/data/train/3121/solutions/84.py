def solve(arr):
    for i in range(len(arr)):
        count = 0
        if arr.count(arr[i]) > 1:
            return arr[i]
        for j in range(len(arr)):
            if arr[i] == (-arr[j]):
                count += 1
        if count != 1: return arr[i]
