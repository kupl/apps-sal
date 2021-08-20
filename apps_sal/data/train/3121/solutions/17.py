def solve(arr):
    nums = []
    unique = 0
    for i in arr:
        if -i in arr:
            nums.append(i)
        else:
            unique = i
    return unique
