def extract(arr): return ''.join(arr[:2] + arr[-2:])


def sort_transform(arr):
    arr = list(map(chr, arr))
    w1 = extract(arr)
    arr.sort()
    w2 = extract(arr)
    return f'{w1}-{w2}-{w2[::-1]}-{w2}'
