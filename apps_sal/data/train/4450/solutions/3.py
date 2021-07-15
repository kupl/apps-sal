def consecutive(arr):
    try:
        return max(arr) - min(arr) - len(arr) + 1
    except:
        return 0
