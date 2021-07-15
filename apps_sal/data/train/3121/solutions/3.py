def solve(arr):
    return [i for i in arr if -i not in arr][0]
