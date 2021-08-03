def find_longest(arr):
    lst = []
    for item in arr:
        lst.append(str(item))
    return int(max(lst, key=len))
