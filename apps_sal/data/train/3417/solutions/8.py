def cut_the_ropes(arr):
    counts = []
    while arr:
        counts.append(len(arr))
        m = min(arr)
        arr = [rope - m for rope in arr if rope - m > 0]
    return counts
