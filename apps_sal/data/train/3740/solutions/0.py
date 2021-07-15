def sort_time(arr):
    arr, s = sorted(arr, key=lambda t: t[0]), []
    while arr:
        nextTP = next((i for i,t in enumerate(arr) if not s or t[0] >= s[-1][1]), 0)
        s.append(arr.pop(nextTP))
    return s
