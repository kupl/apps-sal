def solve(arr):
    for num in arr:
        if arr.count(num) > arr.count(-num):
            return num
        elif arr.count(-num) >  arr.count(num):
            return -num
