def find_longest(arr):
    d = {}
    for i in range(0, len(arr)):
        z = [int(x) for x in str(arr[i])]
        l = len(z)
        s = [str(j) for j in z]
        p = int(''.join(s))
        d.update({p: l})
    m = max(d, key=d.get)
    return m
