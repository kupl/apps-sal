def grab_two(arr, run_sum):
    if len(arr) == 0:
        return run_sum
    else:
        run_sum += arr[0] * arr[-1]
        return grab_two(arr[1:-1], run_sum)


def min_sum(arr):
    arr.sort()
    return grab_two(arr, 0)
