def compound_array(a, b):

    res = []

    for i in range(max(len(a), len(b))):
        res.extend(a[i:i + 1])
        res.extend(b[i:i + 1])

    return res
