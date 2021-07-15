def sect_sort(arr, start, num=0):
    out = arr[:]
    s = slice(start, None if not num else start + num)
    out[s] = sorted(out[s])
    return out
