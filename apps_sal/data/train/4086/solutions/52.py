def first_non_consecutive(arr):
    try:
        return [i for i in arr if not min(arr) + arr.index(i) == i][0]
    except:
        return None
