def solve(arr):
    prev = -1
    for i in arr[-1::-1]:
        if i <= prev:
            arr.remove(i)
        else:
            prev = i
    return arr
