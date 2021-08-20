def hyperrectangularity_properties(arr, d=[]):

    def get(arr, d):
        d.append(len(arr))
        if all((isinstance(i, int) for i in arr)):
            return tuple(d)
        else:
            le = len(arr[0]) if isinstance(arr[0], list) else 0
            if not all((isinstance(i, list) and len(i) == le for i in arr)):
                return
        if get(arr[0], d):
            return tuple(d)
    return get(arr, [])
