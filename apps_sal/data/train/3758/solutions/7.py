def mesh(a, b):
    for i in range(len(b), 0, -1):
        if a.endswith(b[:i]):
            return b[:i]


def word_mesh(arr):
    try:
        return ''.join(mesh(a, b) for a, b in zip(arr, arr[1:]))
    except TypeError:
        return 'failed to mesh'
