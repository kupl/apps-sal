def sum_mix(arr):
    list = []
    for x in arr:
        if isinstance(x, str):
            list.append(int(x))
        if isinstance(x, int):
            list.append(x)
    return sum(list)
    # your code here
