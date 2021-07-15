def consecutive(arr):
    if not arr:
        return 0
    return max(max(arr)-min(arr)-len(arr)+1,0)
