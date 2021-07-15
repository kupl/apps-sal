def solve(arr):
    return [a for i,a in enumerate(arr) if a > max(arr[i+1:]+[0])]
