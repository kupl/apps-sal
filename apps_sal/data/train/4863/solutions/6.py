def circularly_sorted(arr):
    diff = sum(arr[i] > arr[i + 1] for i in range(len(arr) - 1))
    return (diff == 1 and arr[-1] <= arr[0]) or diff == 0
