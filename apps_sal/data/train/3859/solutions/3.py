def odd_one(arr):
    ad = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            ad += 1
            return i
        else:
            pass
    if ad == 0:
        return -1
