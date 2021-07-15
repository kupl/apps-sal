def min_unfairness(arr,k):
    if len(arr) < 2 or k < 2:
        return 0
    t = sorted(arr)
    diff = float('inf')
    for i in range(len(t)-k+1):
        x= t[i+k-1]-t[i]
        if x < diff:
            diff = x
    return diff
