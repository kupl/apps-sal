def solve(arr):
    for i in range(max(arr)+1):
        while arr.count(i)>1:
            arr.remove(i)
    return arr
