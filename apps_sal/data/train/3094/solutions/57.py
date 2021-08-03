def sum_array(arr):
    total = 0
    if not arr:
        return 0
    elif len(arr) <= 2:
        return 0
    else:
        for number in range(0, len(arr)):
            total += arr[number]
            print(total)
        return total - min(arr) - max(arr)
