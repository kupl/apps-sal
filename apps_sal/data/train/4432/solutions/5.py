def can_jump(arr):
    x = len(arr)-1; p = []; i = 0; j = arr[i]; n = i+j
    if not x or not(arr[0]): return False
    while True:
        if x<n: return True
        while j and (n==x or not arr[n]): j -= 1; n = i+j
        if not j:
            if not p: return False
            j = p.pop(); i -= j; j -= 1; continue
        p.append(j); i += j; j = arr[i]; n = i+j

