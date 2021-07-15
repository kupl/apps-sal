def solve(arr):
    
    a = [i for i in arr if arr.count(i) != arr.count(-i)]
    
    return a[0]
