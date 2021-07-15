def solve(arr): 
    return [j for i, j in enumerate(arr) if j not in arr[i+1:]]
