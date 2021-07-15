def sect_sort(arr, st, ln=0):
    return arr[:st] + ( sorted(arr[st:st+ln]) + arr[st+ln:] if ln else sorted(arr[st:]) )
