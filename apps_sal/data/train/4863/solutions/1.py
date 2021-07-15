def circularly_sorted(arr):
    return sum(x > y for x,y in zip(arr, arr[1:]+[arr[0]])) < 2
