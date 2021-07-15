def solve(arr):
    return sum(arr)-max(arr) if max(arr)>sum(arr)-max(arr) else sum(arr)//2
