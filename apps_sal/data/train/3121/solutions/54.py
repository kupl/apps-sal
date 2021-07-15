def solve(arr):
    new_arr = [val for val in arr if not arr.count(-val)]
    return new_arr[0]
