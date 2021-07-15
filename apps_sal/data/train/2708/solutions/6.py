def yes_no(arr):
    counter = 0
    out = []
    _in = []
    while arr:
        for i in arr:
            if counter % 2 == 0:
                out.append(i)
            else:
                _in.append(i)
            counter += 1
        arr = _in
        _in = []
    return out
