def word_mesh(arr):
    (re, e, i) = ('', len(arr[0]), 0)
    while e != 0:
        e -= 1
        if e == 0:
            return 'failed to mesh'
        if arr[i][-e:] == arr[i + 1][:e]:
            re += arr[i][-e:]
            e = len(arr[i])
            i += 1
            if i == len(arr) - 1:
                return re
