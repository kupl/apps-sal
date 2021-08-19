def nth_smallest(arr, pos):
    arr.sort()
    lol = arr[0:pos]
    return lol[pos - 1]
