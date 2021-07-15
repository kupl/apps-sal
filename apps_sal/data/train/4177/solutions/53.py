def men_from_boys(arr):
    arr = set(arr)
    return sorted([i for i in arr if not i % 2]) + sorted([i for i in arr if  i % 2],reverse=True)
