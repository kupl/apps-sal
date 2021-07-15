def first_non_consecutive(arr):
    expected = arr[0]
    for x in arr:
        if x != expected:
            return x
        else:
            expected += 1

