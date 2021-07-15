def pick_peaks(arr):
    p = []
    z = []
    res = {"pos": [], "peaks": []}
    for i, k in enumerate(arr[1:-1]):
        if k > arr[i] and k > arr[i+2]:
            p.append(i+1)
            z.append(k)
        elif k == arr[i+2] and k > arr[i]:
            n = 1
            while True:
                n += 1
                if k != arr[i+n] or i+n == len(arr)-1:
                    break
            if k > arr[i+n]:
                p.append(i+1)
                z.append(k)
    res["pos"] = p
    res["peaks"] = z
    return res
