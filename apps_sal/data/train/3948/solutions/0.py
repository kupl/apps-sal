def sel_reverse(arr,l):
    return [ elt for i in range(0, len(arr), l) for elt in arr[i:i+l][::-1] ] if l != 0 else arr
