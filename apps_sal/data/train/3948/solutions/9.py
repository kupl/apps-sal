def sel_reverse(arr, l):
    return [y for x in [arr[i:i + l][::-1] for i in range(0, len(arr), l)] for y in x] if l else arr
