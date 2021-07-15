def greatest_distance(arr):
    res = 0
    for i, x in enumerate(arr): 
        for j, y in enumerate(arr): 
            if y==x: 
                res = max(res, abs(i-j))
    return res
