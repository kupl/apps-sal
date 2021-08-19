def solve(arr):
    arr = sorted(arr, reverse=True)
    new_list = []
    boolean = True
    while len(arr) >= 1:
        new_list.append(arr[0])
        if boolean == True:
            boolean = False
        else:
            boolean = True
        arr.pop(0)
        arr = sorted(arr, reverse=boolean)
    return new_list
