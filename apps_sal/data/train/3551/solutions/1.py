def array_previous_less(arr):
    out = []
    
    for i, n in enumerate(arr):
        x = -1
        for m in arr[:i][::-1]:
            if m < n:
                x = m
                break
        out.append(x)
    
    return out
