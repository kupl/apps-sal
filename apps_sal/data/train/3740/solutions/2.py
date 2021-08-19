def sort_time(arr):
    arr, prv, result = sorted(arr, key=lambda p: p[0]), "00:00", []
    while arr:
        nxt = next((p for p in arr if p[0] >= prv), arr[0])
        result.append(nxt)
        arr.remove(nxt)
        prv = nxt[1]
    return result


# more compact but less readable:
#    while arr:
#        result.append(arr.pop(next((i for i, p in enumerate(arr) if p[0] >= prv), 0)))
#        prv = result[-1][1]
