def sort_transform(arr):
    arr_al = sorted([chr(x) for x in arr])
    return '-'.join([chr(arr[0]) + chr(arr[1]) + chr(arr[-2]) + chr(arr[-1]),
                     chr(sorted(arr)[0]) + chr(sorted(arr)[1]) + chr(sorted(arr)[-2]) + chr(sorted(arr)[-1]),
                     chr(sorted(arr, reverse=True)[0]) + chr(sorted(arr, reverse=True)[1]) + chr(sorted(arr, reverse=True)[-2]) + chr(sorted(arr, reverse=True)[-1]),
                     arr_al[0] + arr_al[1] + arr_al[-2] + arr_al[-1]])
