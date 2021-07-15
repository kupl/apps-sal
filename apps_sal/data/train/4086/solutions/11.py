def first_non_consecutive(arr):
    a = [x+1 for x in range(min(arr), max(arr)+1) if x not in arr]
    return None if a == [] else a[0]
