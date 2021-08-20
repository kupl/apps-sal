def elements_sum(arr, d=0):
    return sum([d if not arr[x] or len(arr[x]) <= len(arr) - x - 1 else arr[x][len(arr) - x - 1] for x in range(len(arr))])
