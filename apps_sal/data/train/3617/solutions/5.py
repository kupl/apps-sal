def is_zero_balanced(arr):
    return all(arr.count(i)==arr.count(-i) for i in arr) if arr else False
