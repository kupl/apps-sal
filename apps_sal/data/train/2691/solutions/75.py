def solve(arr):
    l = len(arr)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = arr[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = arr[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    return max(integ)
