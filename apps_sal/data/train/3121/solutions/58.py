def solve(arr):
    a = 1
    for i in arr:
        if arr.count(i) > 1:
            a = arr.count(i)  
    return sum(arr) / a
