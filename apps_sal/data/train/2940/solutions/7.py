def repeats(arr):
    return sum(num for num in arr if arr.count(num) == 1)
