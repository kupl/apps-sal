def get_offsets(distance, moore=True):
    offsets = list(range(-distance, distance + 1))
    for dr in offsets:
        for dc in offsets:
            if (dr, dc) == (0, 0):
                continue
            if not moore and abs(dr) + abs(dc) > distance:
                continue
            yield (dr, dc)


def get_neighbourhood(n_type, arr, coordinates, distance=1):
    h, w = len(arr), len(arr[0])
    if not (0 <= coordinates[0] < h and 0 <= coordinates[1] < w):
        return []
    r, c = coordinates
    return [
        arr[r + dr][c + dc]
        for dr, dc in get_offsets(distance, n_type == 'moore')
        if 0 <= r + dr < h and 0 <= c + dc < w
    ]
