def find_smallest_int(arr):
    minor = arr[0]
    for el in arr:
        if el < minor:
            minor = el
            print(minor)
    return minor
